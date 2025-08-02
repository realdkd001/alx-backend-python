from rest_framework.permissions import IsAuthenticated
from .permission import IsOwnerOrAdmin
from rest_framework import viewsets
from .models import Message, User

from .serializers import MessageSerializer, UserSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]