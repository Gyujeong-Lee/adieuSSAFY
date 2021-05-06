from django.db import models


# Bonus - 유튜브 채팅용 데이터 모델들
class ChatUser(models.Model):
    name = models.CharField(max_length=10)
    initial = models.CharField(max_length=2)
    fg_color = models.CharField(max_length=8)
    bg_color = models.CharField(max_length=8)

    def __str__(self):
        return self.name
    
class ChatMessage(models.Model):
    chat_user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.chat_user.name +"|"+ self.message
    