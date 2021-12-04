from rest_framework import serializers
from .models import InjuryReport, Team, UserPlayer

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