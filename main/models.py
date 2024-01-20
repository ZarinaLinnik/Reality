from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):

    class Meta:
        abstract = True

    changes = models.TextField(blank=True)
    what_why_how = models.TextField(blank=True)
    date_time = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class ParameterIMGMyPhoto(models.Model):

    class Meta:
        verbose_name_plural = 'MyPhoto'

    image = models.ImageField(upload_to='uploaded')
    date_time_pict = models.DateTimeField(blank=True)
    date_time = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Parameter1WhoAreYou(BaseModel):

    class Meta:
        verbose_name_plural = 'Parameter1WhoAreYou'
    
    name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    goals = models.TextField(blank=True)


class Parameter2WhatDoYouDo(BaseModel): 

    class Meta:
        verbose_name_plural = 'Parameter2WhatDoYouDo'


class Parameter3Environment(BaseModel): 

    class Meta:
        verbose_name_plural = 'Parameter3Environment'


class Parameter4Habits(BaseModel): 

    class Meta:
        verbose_name_plural = 'Parameter4Habits'


class Parameter5FreeTime(BaseModel): 

    class Meta:
        verbose_name_plural = 'Parameter5FreeTime'


class Parameter6LookLike(BaseModel): 

    class Meta:
        verbose_name_plural = 'Parameter6LookLike'


class Parameter7Behavior(BaseModel): 

    class Meta:
        verbose_name_plural = 'Parameter7Behavior'


class Parameter8ThoughtsDirection(BaseModel): 

    class Meta:
        verbose_name_plural = 'Parameter8ThoughtsDirection'
