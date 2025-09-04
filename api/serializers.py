from rest_framework import serializers
from .models import Meal, Rating

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