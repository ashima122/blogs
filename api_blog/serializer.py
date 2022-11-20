from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from new_blog.models import * 
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# Register serializer
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    profile_pic = serializers.ImageField()

class PostBlogSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()

    
class GetBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = '__all__'