from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password')
        extra_kwargs={'password': {'write_only':True, 'required':True}} 
    
    def create(self, validated_data): #overwrite built in create fn.
        # create new instance of the model
        user=User.objects.create(**validated_data)
        return user

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'title','details','deadline',)
       
    def create(self, validated_data): #overwrite built in create fn.
        # create new instance of the model
        reminder=Reminder.objects.create(**validated_data)
        return reminder
    
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"