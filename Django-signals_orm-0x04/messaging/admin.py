from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Message)
admin.site.register(models.Notification)
admin.site.register(models.MessageHistory)