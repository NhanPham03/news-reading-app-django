from django.db import models
from django.conf import settings
from apps.articles.models import Article

class Notification(models.Model):
  recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
  message = models.TextField(max_length=255)
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='notifications')
  timestamp = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'notifications'
