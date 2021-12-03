from rest_framework import serializers
from .models import UserPlayer

class UserPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlayer
        fields = ['playerId', 'User']