from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class UserPlayer(models.Model):
    playerId = models.CharField(max_length=50, blank=True)
    User = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
