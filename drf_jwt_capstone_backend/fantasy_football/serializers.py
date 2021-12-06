from rest_framework import serializers
from .models import CommentBoard, InjuryReport, Team, UserPlayer

class UserPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlayer
        fields = ['PlayerId', 'User']

class InjuryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InjuryReport
        fields = ['playerTeam', 'playerName', 'injury', 'duration']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['TeamName', 'PlayerPosition', 'UserPlayer']

class CommentBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentBoard
        fields = ['Comment','UserPlayer']

# class UserPreferenceSerializer(serializers.ModelSerializer):
#     class Mega:
#         model = UserPreference
#         fields = ['UserPlayer', 'CommentBoard', 'Value', 'Date']