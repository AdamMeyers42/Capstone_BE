from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class UserPlayer(models.Model):
    playerId = models.CharField(max_length=50, blank=True)
    userId = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, db_column='userId')

class InjuryReport(models.Model):
    playerTeam = models.CharField(max_length=50, blank=True)
    playerName= models.CharField(max_length=50, blank=True)
    injury = models.CharField(max_length=50, blank=True)
    duration = models.CharField(max_length=50, blank=True)

class Team(models.Model):
    teamName = models.CharField(max_length=50, blank=True)
    playerPosition = models.CharField(max_length=20, blank=True)
    userPlayerId = models.ForeignKey(UserPlayer, null=True, on_delete=models.CASCADE, db_column='userPlayerId')

class CommentBoard(models.Model):
    comment = models.TextField(max_length=200, blank=True)
    userId = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, db_column='userId')

class Comment:
  def __init__(self, username, comment, commentId):
    self.commentId = commentId
    self.username = username
    self.comment = comment

# class UserPreference(models.Model):
#     UserPlayer = models.ForeignKey(UserPlayer)
#     CommentBoard = models.ForeignKey(CommentBoard)
#     value = models.IntegerField(default=0)
#     date = models.DateTimeField(auto_now=True)


