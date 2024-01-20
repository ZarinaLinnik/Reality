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


class Parameter2WhatDoYouDo(models.Model): 

    class Meta:
        verbose_name_plural = 'Parameter2WhatDoYouDo'

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Parameter3Environment(models.Model): 

    class Meta:
        verbose_name_plural = 'Parameter3Environment'

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Parameter4Habits(models.Model): 

    class Meta:
        verbose_name_plural = 'Parameter4Habits'

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Parameter5FreeTime(models.Model): 

    class Meta:
        verbose_name_plural = 'Parameter5FreeTime'

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Parameter6LookLike(models.Model): 

    class Meta:
        verbose_name_plural = 'Parameter6LookLike'

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Parameter7Behavior(models.Model): 

    class Meta:
        verbose_name_plural = 'Parameter7Behavior'

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Parameter8ThoughtsDirection(models.Model): 

    class Meta:
        verbose_name_plural = 'Parameter8ThoughtsDirection'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class ParameterIMGMyPhoto(models.Model):

    class Meta:
        verbose_name_plural = 'MyPhoto'

    image = models.ImageField(upload_to='uploaded')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
