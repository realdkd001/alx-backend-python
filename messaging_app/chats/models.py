from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(null=False, max_length=150)
    last_name = models.CharField(null=False, max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(null=False, max_length=128, blank=False)
    phone_number = models.CharField(max_length=15, unique=True, null=False) 
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True,default=uuid4, unique=True, null=False, editable=False )
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Converation {self.conversation_id}"

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, null=False)
    conversation= models.ForeignKey(Conversation, null=False, related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender}: {self.message_body[:30]}..."
