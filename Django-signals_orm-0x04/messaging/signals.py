from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory, User

@receiver(post_save, sender=Message)
def new_message(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)
        

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:
        old_message = Message.objects.get(pk=instance.pk)
        
        if old_message.content != instance.content:
            
            MessageHistory.objects.create(
                message = instance,
                edited_by =instance.sender,
                old_content = old_message.content
            )
            
            instance.edited = True
        
@receiver(post_delete, sender=User)
def post_delete_user(sender, instance, **kwargs):
    MessageHistory.objects.filter(edited_by=instance).delete()