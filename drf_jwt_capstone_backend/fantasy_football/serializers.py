from rest_framework import serializers
from .models import CommentBoard, InjuryReport, Team, UserPlayer

class UserPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlayer
        fields = ['playerId', 'User']

class InjuryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InjuryReport
        fields = ['playerTeam', 'playerName', 'injury', 'duration']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['teamName', 'playerPosition', 'UserPlayer']

class CommentBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentBoard
        fields = ['comment','User_id']

# class UserPreferenceSerializer(serializers.ModelSerializer):
#     class Mega:
#         model = UserPreference
#         fields = ['UserPlayer', 'CommentBoard', 'Value', 'Date']