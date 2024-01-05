from django.contrib.auth.models import User
from django.db import models


class Parameter1WhoAreYou(models.Model):

    class Meta:
        verbose_name_plural = 'Parameter1WhoAreYou'
    
    name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    goals = models.TextField(blank=True)
    changes = models.TextField(blank=True)
    what_why_how = models.TextField(blank=True)
    date_time = models.DateTimeField()

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class ParameterIMGMyPhoto(models.Model):

    class Meta:
        verbose_name_plural = 'MyPhoto'

    image = models.ImageField(upload_to='uploaded')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
