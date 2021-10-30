from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.templatetags.static import static
import os

def get_image_path(instance, filename):
    return os.path.join('users', str(instance.id), filename)


class Profile(models.Model):
    
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    avatar = models.ImageField(upload_to=get_image_path, default='https://github.com/yogesh-naik/Wayfarer/blob/avatar/Nitelife/main_app/static/images/user.png')
    birthday = models.DateField(null=True, blank=True)
    number = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    bio = models.CharField(max_length=500, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')



class Event(models.Model):

    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, serialize=True, related_name='creator', null=True)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    bio = models.TextField(max_length=500, blank=True)
    image = models.CharField(max_length=500, blank=True)
    video = models.FileField(upload_to='media', blank=True)

    def __str__(self):
        return self.title

