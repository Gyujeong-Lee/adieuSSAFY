from django.contrib import admin
from .models import ChatUser, ChatMessage

# Register your models here.

# Bonus
admin.site.register(ChatUser)
admin.site.register(ChatMessage)