from django.db import models

# Create your models here.

# class Event(models.Event):

#     creator = models.ForeignKey(User, on_delete=models.CASCADE, serialize=True, related_name='creator')
#     title = models.CharField(max_length=255, required=True)
#     location = models.CharField(max_length=255, required=True)
#     bio = models.TextField(max_length=500, blank=True)
#     image = models.ImageField()
#     guest = models.ForeignKey(User, on_delete=models.CASCADE, serialize=True, related_name='guest')

#     def __str__(self):
#         return self.title