from rest_framework import serializers
from ..models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'first_name']

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid username or password.')
        attrs['user'] = user
        return attrs
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'user')
        )
        return user
