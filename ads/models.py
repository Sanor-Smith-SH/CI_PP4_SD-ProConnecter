from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    contact_info = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name.username

class Service(models.Model):
    ads_author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    occupation = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)
    featured_image = CloudinaryField('image', default='placeholder')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
