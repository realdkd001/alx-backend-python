from .models import Message, User
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"