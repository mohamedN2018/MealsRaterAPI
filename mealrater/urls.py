from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLResolver, URLPattern

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
