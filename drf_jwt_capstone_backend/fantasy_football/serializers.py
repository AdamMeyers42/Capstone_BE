from rest_framework import serializers
from .models import CommentBoard, InjuryReport, Team, UserPlayer, UserPreference

class UserPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlayer
        fields = ['playerId', 'User']

class InjuryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InjuryReport
        fields = ['injury', 'duration', 'userPlayer']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['teamName', 'playerPosition', 'userPlayer']

class CommentBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentBoard
        fields = ['comment','userPlayer']

class UserPreferenceSerializer(serializers.ModelSerializer):
    class Mega:
        model = UserPreference
        fields = ['userPlayer', 'commentBoard', 'value', 'date']