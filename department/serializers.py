
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Baseuser, Project

class BaseuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baseuser
        fields = ['userType', 'name', 'email', 'password', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}  # Password should not be read in response

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))  # Hash the password
        return super().create(validated_data)
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baseuser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Password should not be read in response
    

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baseuser
        fields = ['password']
        extra_kwargs = {'password': {'write_only': True}}
