from contextvars import Token
from rest_framework import serializers
from .models import Meal, Rating
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            token = Token.objects.create(user=user)
            return token

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'title', 'description', 'on_of_rating', 'avg_rating', 'image', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'meal', 'user', 'stars', 'created_at']
        read_only_fields = ['created_at']