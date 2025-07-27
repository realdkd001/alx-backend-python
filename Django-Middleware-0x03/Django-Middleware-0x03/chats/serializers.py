from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField()
    phone_number = serializers.CharField(
        required=True,
        max_length=15,
        help_text="Phone number must be 15 digits"
    )
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number']
        read_only_fields = ['user_id']
    
    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        return value

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    sender_email = serializers.SerializerMethodField()
    sender_full_name = serializers.SerializerMethodField()
    sender_contact = serializers.SerializerMethodField()
    message_body = serializers.CharField(required=True)

    class Meta:
        model = Message
        fields = ['message_id', 'conversation', 'sender_email', 'sender', 'sender_contact', 'sender_full_name', 'message_body', 'sent_at']
        read_only_fields = ['message_id', 'sent_at']
        
    def get_sender_full_name(self, obj):
        return f"{obj.sender.first_name} {obj.sender.last_name}"
    
    def get_sender_email(self, obj):
        return obj.sender.email
    
    def get_sender_contact(self, obj):
        return obj.sender.phone_number

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants','name', 'messages', 'created_at']
     