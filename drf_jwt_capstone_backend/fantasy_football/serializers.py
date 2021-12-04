from rest_framework import serializers
from .models import InjuryReport, UserPlayer

class UserPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlayer
        fields = ['playerId', 'User']

class InjuryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InjuryReport
        fields = ['injury', 'duration', 'userplayer']