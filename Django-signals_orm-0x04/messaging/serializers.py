from .models import Message, User
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'timestamp', 'edited', 'parent_message', 'replies']

    def get_replies(self, obj):
        # Recursive serialization
        if obj.replies.exists():
            return MessageSerializer(obj.replies.all(), many=True).data
        return []

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"