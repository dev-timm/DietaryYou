from django.db import models
from django.contrib.auth.models import User
from cloudinary. models import CloudinaryField


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='placeholder')
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    hobbies = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    class Meta:
        ordering = ['full_name']
