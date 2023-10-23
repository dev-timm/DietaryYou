from django.db import models
from django.contrib.auth.models import User
from cloudinary. models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    hobbies = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    class Meta:
        ordering = ['full_name']

    def save(self, *args, **kwargs):
        self.slug = self.user.username
        super(UserProfile, self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def set_up_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
