from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response 
from rest_framework import serializers, status
from rest_framework.views import APIView
from django.http.response import HttpResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CommentBoard, UserPlayer, InjuryReport, Team, Comment
from .serializers import CommentBoardSerializer, PlayerDetailSerializer, PlayerSerializer, UserPlayerSerializer, InjuryReportSerializer, TeamSerializer, CommentSerializer
import requests
import json

class InjuryReports(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        injury = InjuryReport.objects.all()
        serializer = InjuryReportSerializer(injury, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return InjuryReport.objects.get(pk=pk)
        except InjuryReport.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def post(self, request):
        serializer = InjuryReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        update_injury = self.get_object(pk)
        serializer = InjuryReportSerializer(update_injury, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_injury = self.get_object(pk)
        delete_injury.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentBoards(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        comments = []
        for c in CommentBoard.objects.all():
            comments.append(Comment(c.userId, c.comment, c.id))
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentBoardsAuthenticated(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = CommentBoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_comment(self, pk):
        try:
            return CommentBoard.objects.get(pk=pk)
        except CommentBoard.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def delete(self, request, pk):
        delete_comment = self.get_comment(pk)
        delete_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Teams(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self,request):
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data)
    
    def get_userteam(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        delete_team = self.get_userteam(pk)
        delete_team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserPlayers(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self,request):
        team = UserPlayer.objects.all()
        serializer = UserPlayerSerializer(team, many=True)
        return Response(serializer.data)
 
    def get_userplayer(self, pk):
        try:
            return UserPlayer.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    # def post(self, request):
    #     serializer = UserPlayerSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     teamJson = '{"teamName":"my cool team", "playerPosition":"QB" "userPlayer":7}'
    #     # team = Team()
    #     teamSerializer = TeamSerializer(data=teamJson)
    #     if teamSerializer.is_valid():
    #         teamSerializer.save()
    #         # return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        delete_userplayer = self.get_userplayer(pk)
        delete_userplayer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Players(APIView):

    def get(self,request):
        headers = {'Authorization': 'Basic MDA1ZWY3YTAtZmFhMC00YTE4LTkwOTItYjM1NWQwOk1ZU1BPUlRTRkVFRFM='}
        r = requests.get('https://api.mysportsfeeds.com/v2.1/pull/nfl/players.json?limit=10', headers=headers)
        data = json.loads(r.text)
        players = data.get('players')
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserPlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        teamName = request.data.get("teamName")
        playerPosition = request.data.get("playerPosition")
        userId = request.data.get("userId")
        playerId = request.data.get("playerId")
        userPlayer = UserPlayer.objects.get(userId = userId, playerId = playerId)   
        userPlayerId = userPlayer.id
        teamJson = f'{{"teamName":"{teamName}", "playerPosition":"{playerPosition}", "userPlayerId":{userPlayerId}}}'
        # team = Team()
        test = json.loads(teamJson)
        teamSerializer = TeamSerializer(data=test)
        if teamSerializer.is_valid():
            teamSerializer.save()
            return Response(teamSerializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

