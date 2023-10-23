from rest_framework import serializers
from .models import UserModel, MessageModel
from django.contrib.auth import get_user_model

class CustomSerializer (serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
    
class MessageSerializer (serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'