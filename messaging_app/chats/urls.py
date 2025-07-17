from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from .views import ConversationViewSet, MessageViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Nest messages under conversations
convo_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
convo_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = router.urls + convo_router.urls
