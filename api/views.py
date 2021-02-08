from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions,generics
from . import serializers
from . permissions import ReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from django.http import HttpResponse

# Create your views here.

class FileList(generics.ListCreateAPIView):
    queryset=File.objects.all()
    serializer_class=serializers.FileSerializer

    #lets overwrite post fn
    def post(self, request, *args, **kwargs):
        name=request.data['name']
        image=request.data['image']
        File.objects.create(name=name, image=image)
        return HttpResponse(status=200)

class ReminderList(generics.ListCreateAPIView):
    queryset=Reminder.objects.all()
    serializer_class=serializers.ReminderSerializer
    # permission_classes=(IsAuthenticated,)

class UserList(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=serializers.UserSerializer

class UserViewSet(viewsets.ModelViewSet):#class that handles all CRUD ops on the User model
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class=serializers.UserSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    # permission_classes=(ReadOnly)
     


from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = serializers.FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)