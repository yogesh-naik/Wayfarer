from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):

    creator = models.ForeignKey(User, on_delete=models.CASCADE, serialize=True, related_name='creator')
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    bio = models.TextField(max_length=500, blank=True)
    image = models.CharField(max_length=500, blank=True)
    guest = models.ForeignKey(User, on_delete=models.CASCADE, serialize=True, related_name='guest')

    def __str__(self):
        return self.title