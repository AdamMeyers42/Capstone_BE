from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response 
from rest_framework import status
from rest_framework.views import APIView
from django.http.response import HttpResponse
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import CommentBoard, UserPlayer, InjuryReport, Team
from .serializers import CommentBoardSerializer, UserPlayerSerializer, InjuryReportSerializer, TeamSerializer



class InjuryReports(APIView):

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

    def get(self, request):
        comments = CommentBoard.objects.all()
        serializer = CommentBoardSerializer(comments, many=True)
        return Response(serializer.data)
    
    def get_comment(self, pk):
        try:
            return CommentBoard.objects.get(pk=pk)
        except CommentBoard.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    def post(self, request):
        serializer = CommentBoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        delete_comment = self.get_comment(pk)
        delete_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Teams(APIView):

    def get(self,request):
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)