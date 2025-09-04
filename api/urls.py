from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MealViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'meals', MealViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
