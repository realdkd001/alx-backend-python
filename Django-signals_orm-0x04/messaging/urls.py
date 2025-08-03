from django.urls import path
from .views import list_messages, create_message, delete_user, unread_messages

urlpatterns = [
    path('messages/', list_messages, name='list_messages'),
    path('messages/create/', create_message, name='create_message'),
    path('delete_user/', delete_user, name='delete_user'),
    path('messages/unread/', unread_messages, name='unread-messages')
]
