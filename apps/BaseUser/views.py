from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers
from rest_framework import serializers
from rest_framework.views import APIView
from .models import BaseUser
from .serializers import BaseUserSerializer

def GetUserInfo(request):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer(queryset,many=True)
    return JsonResponse(serializer_class.data,safe = False )