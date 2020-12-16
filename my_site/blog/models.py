from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, default='Default title')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Questions(models.Model):
    title = models.CharField(max_length=100, default='Unnamed question')
    text = models.TextField()
    answer = models.TextField(default='No answer yet')

    def __str__(self):
        return self.title
