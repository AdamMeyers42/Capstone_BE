from rest_framework import serializers
from .models import CommentBoard, InjuryReport, Team, UserPlayer, Comment

class UserPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlayer
        fields = ['playerId', 'userId']

class InjuryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InjuryReport
        fields = ['playerTeam', 'playerName', 'injury', 'duration']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['teamName', 'playerPosition', 'userPlayerId']

class CommentBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentBoard
        fields = ['comment','userId']

class CommentSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    comment = serializers.CharField(max_length=200)
    commentId = serializers.IntegerField()


# class UserPreferenceSerializer(serializers.ModelSerializer):
#     class Mega:
#         model = UserPreference
#         fields = ['UserPlayer', 'CommentBoard', 'Value', 'Date']