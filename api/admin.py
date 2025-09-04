from django.contrib import admin

# Register your models here.

from .models import Meal, Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'meal', 'stars', 'created_at')
    search_fields = ('user__username', 'meal__title')
    list_filter = ('meal', 'user', 'stars', 'created_at')


class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description',)
    list_filter = ('title', 'description', 'created_at',)


admin.site.register(Rating, RatingAdmin)
admin.site.register(Meal, MealAdmin)
