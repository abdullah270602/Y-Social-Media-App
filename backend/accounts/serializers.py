from datetime import timedelta
from .models import EmailVerification, User
from rest_framework import serializers  # type: ignore
from django.urls import reverse
from django.utils import timezone


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password','date_of_birth']


    def validate_email(self, value):    
        """
        Check that the email is not already in use.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value


    def create(self, validated_data):
        """
        Create a new User instance with the validated data.
        """
        user = User(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
            date_of_birth=validated_data['date_of_birth']
        )
        user.set_password(validated_data['password'])
        
        user.save()
        
        EmailVerification.objects.create(
            user=user,
            token = EmailVerification.generate_token(),
            token_expiration=timezone.now() + timedelta(hours=6)  # Token expires in 6 hours
        )
        
        
        
        return user


class UserInfoSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ['full_name', 'email', 'username','date_of_birth']
        
        
class UserFollowingFollowersSerializerCount(serializers.Serializer):
    following_count = serializers.IntegerField()
    followers_count = serializers.IntegerField()   
        
        
class UserFollowingSerializer(serializers.Serializer):
    following = serializers.ListField()