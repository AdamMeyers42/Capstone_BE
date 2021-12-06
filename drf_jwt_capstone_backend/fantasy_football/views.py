from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response 
from rest_framework import status
from rest_framework.views import APIView
from django.http.response import HttpResponse
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import UserPlayer, InjuryReport, Team
from .serializers import UserPlayerSerializer, InjuryReportSerializer, TeamSerializer



class InjuryReport(APIView):

    def get(self, request):
        injury = InjuryReport.objects.all()
        serializer = InjuryReportSerializer(injury, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InjuryReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)