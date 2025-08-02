from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, delete_user
from django.urls import path

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('delete_user/', delete_user, name='delete_user'), 
]
