from datetime import datetime, time, timedelta
import logging
from django.http import HttpResponseForbidden, JsonResponse
from collections import defaultdict
import threading

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Set up basic logging
        logging.basicConfig(
            filename='requests.log',
            level=logging.INFO,
            format='%(message)s',
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_message)

        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = datetime.now().time()
        start_time = time(18, 0)  # 6:00 PM
        end_time = time(21, 0)    # 9:00 PM

        if not (start_time <= now <= end_time):
            return HttpResponseForbidden("⛔ Access to the messaging app is only allowed between 6 PM and 9 PM.")

        return self.get_response(request)


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_log = defaultdict(list)  # Stores request timestamps per IP
        self.lock = threading.Lock()          # Ensures thread safety

    def __call__(self, request):
        # Apply only to POST requests to /api/messages
        if request.method == "POST" and request.path.startswith("/api/messages"):
            ip = self.get_client_ip(request)
            now = datetime.now()

            with self.lock:
                # Remove timestamps older than 1 minute
                self.request_log[ip] = [t for t in self.request_log[ip] if now - t < timedelta(minutes=1)]

                if len(self.request_log[ip]) >= 5:
                    return JsonResponse(
                        {"error": "Rate limit exceeded. Max 5 messages per minute."},
                        status=429
                    )

                self.request_log[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Restrict critical actions (delete/update)
        if request.method in ['DELETE', 'PUT', 'PATCH']:
            user = request.user

            if not user.is_authenticated:
                return HttpResponseForbidden("⛔ You must be authenticated to perform this action.")

            is_admin = user.is_superuser
            is_moderator = user.groups.filter(name="moderator").exists()

            if not (is_admin or is_moderator):
                return HttpResponseForbidden("⛔ Access denied: Only admins or moderators can perform this action.")

        return self.get_response(request)
