from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='meal_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def on_of_rating(self):
        ratings = Rating.objects.filter(meal=self)
        return len(ratings)
    

    def avg_rating(self):
        # sum of rating stars / len of rating how many rating
        sum = 0
        ratings = Rating.objects.filter(meal=self) # no of rating happend to the meal
        for x in ratings:
            sum += x.stars

        if len(ratings) > 0:
            return sum / len(ratings)
        else: 
            return 0 # if there is no rating return 

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Meals'
        verbose_name = 'Meal'


    def __str__(self):
        return self.title

class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} rated {self.meal.title} {self.stars} stars"
    def save(self, *args, **kwargs):
        if self.stars < 1 or self.stars > 5:
            raise ValueError("Stars must be between 1 and 5")
        super().save(*args, **kwargs)
        return f"{self.user.username} rated {self.meal.title} {self.stars} stars"
    
    class Meta:
        unique_together = ('user', 'meal')
        # index_together = ['user', 'meal']
        verbose_name_plural = 'Ratings'
        verbose_name = 'Rating'