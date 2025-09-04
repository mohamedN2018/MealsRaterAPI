from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import permissions, status



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            '''
            create or update
            '''
            meal = Meal.objects.get(pk=pk)
            stars = request.data['stars']
            user = request.user
            try:
                # update
                rate = Rating.objects.get(user=user.id, meal=meal.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'meal Rating updated successfully',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_400_BAD_REQUEST)

            except:
                # create if the rating does not exist
                 
                rating = Rating.objects.create(
                    user=user,
                    meal=meal,
                    stars=stars
                )
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'meal Rating create successfully',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_201_CREATED)

        else:
            json = {
                'message': 'stars not provided'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        Response = {
            'message': 'This is how you should update a rating'
        }
        return Response(Response, status=status.HTTP_400_BAD_REQUEST)
    def create(self, request, *args, **kwargs):
        Response = {
            'message': 'This is how you should update a rating'
        }
        return Response(Response, status=status.HTTP_400_BAD_REQUEST)
