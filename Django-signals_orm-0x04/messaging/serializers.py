from .models import Message, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'first_name', 'last_name']


class MessageSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    sender = UserSerializer(read_only=True)
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # <-- writeable

    class Meta:
        model = Message
        fields = [
            'id', 'sender', 'receiver', 'content', 'timestamp', "read",
            'edited', 'parent_message', 'replies'
        ]

    def get_replies(self, obj):
        children = obj.replies.all()
        if children.exists():
            return MessageSerializer(children, many=True, context=self.context).data
        return []
