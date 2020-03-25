from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets

from .models import CoronaData, CountryData
from .serializers import CoronaDataSerializer, CountryDataSerializer

import datetime

class CoronaDataViewSet(viewsets.ModelViewSet):
    now = datetime.datetime.now()

    queryset = CoronaData.objects.all().order_by('-created_at')
    serializer_class = CoronaDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class CoronaDataCurrentViewSet(viewsets.ModelViewSet):
    queryset = CoronaData.objects.all().order_by('-created_at')[:1]
    serializer_class = CoronaDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class CountryDataViewSet(viewsets.ModelViewSet):
    queryset = CountryData.objects.all().order_by('-total_case')
    serializer_class = CountryDataSerializer
    permission_classes = [permissions.IsAuthenticated]