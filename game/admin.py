from django.contrib import admin
from .models import ChatUser, ChatMessage, Card, BalanceGame

# Register your models here.

# Bonus
admin.site.register(ChatUser)
admin.site.register(ChatMessage)

# game2
admin.site.register(Card)
admin.site.register(BalanceGame)