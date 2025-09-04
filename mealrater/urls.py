from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLResolver, URLPattern
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('tokenrequest/', obtain_auth_token, name='api_token_request')
]
