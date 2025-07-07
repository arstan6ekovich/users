from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Users (models.Model):
    user_name = models.CharField(max_length=32)
    user_phone = models.PositiveIntegerField()
    user_age = models.PositiveSmallIntegerField(validators=[MinValueValidator(16), MaxValueValidator(60)])
    user_description = models.TextField()
    user_city = models.CharField(max_length=32)
    user_image = models.ImageField(upload_to='user_image/')


