from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['userType', 'name', 'email', 'password', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
            return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

class ChangePasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['password']
        extra_kwargs = {'password': {'write_only': True}}

class RegiterSerializer(serializers.ModelSerializer):
    confirmPass = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password', 'confirmPass', 'userType', 'is_active')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
        }

    def validate(self, data):
        password = data.get('password')
        confirmPass = data.get('confirmPass')

        if password!= confirmPass:
            raise serializers.ValidationError({'DOES NOT MATCH': 'Password and confirmPass does not match'})
        return data
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)