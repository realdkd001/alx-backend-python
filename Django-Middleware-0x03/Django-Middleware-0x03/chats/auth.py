from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

token_obtain_pair = TokenObtainPairView.as_view()
token_refresh = TokenRefreshView.as_view()
