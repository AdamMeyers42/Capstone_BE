from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class UserPlayer(models.Model):
    playerId = models.CharField(max_length=50, blank=True)
    User = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

class InjuryReport(models.Model):
    injury = models.CharField(max_length=50, blank=True)
    duration = models.CharField(max_length=50, blank=True)
    UserPlayer = models.ForeignKey(UserPlayer)

class Team(models.Model):
    teamName = models.CharField(max_length=50, blank=True)
    playerPosition = models.CharField(max_length=20, blank=True)
    UserPlayer = models.ForeignKey(UserPlayer)

class CommentBoard(models.Model):
    comment = models.CharField(max_length=50, blank=True)
    UserPlayer = models.ForeignKey(UserPlayer)

class UserPreference(models.Model):
    UserPlayer = models.ForeignKey(UserPlayer)
    CommentBoard = models.ForeignKey(CommentBoard)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

