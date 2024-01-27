from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    """
    Base model for other models.
    """

    class Meta:
        abstract = True

    text0 = models.TextField(blank=True)
    changes = models.TextField(blank=True)
    what_why_how = models.TextField(blank=True)
    date_time = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class TextModel(BaseModel):
    """
    Base model with text fields.
    """

    class Meta:
        abstract = True

    text1 = models.TextField(blank=True)
    text2 = models.TextField(blank=True)
    text3 = models.TextField(blank=True)
    text4 = models.TextField(blank=True)


class ParameterIMGMyPhoto(models.Model):

    class Meta:
        verbose_name_plural = 'MyPhoto'

    image = models.ImageField(upload_to='uploaded')
    date_time_pict = models.DateTimeField(max_length=16)
    date_time = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Parameter1WhoAreYou(BaseModel):

    class Meta:
        verbose_name_plural = 'Parameter1WhoAreYou'
    
    name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    goals = models.TextField(blank=True)


class Parameter2WhatDoYouDo(TextModel): 

    class Meta:
        verbose_name_plural = 'Parameter2WhatDoYouDo'


class Parameter3Environment(TextModel): 

    class Meta:
        verbose_name_plural = 'Parameter3Environment'


class Parameter4Habits(TextModel): 

    class Meta:
        verbose_name_plural = 'Parameter4Habits'


class Parameter5FreeTime(TextModel): 

    class Meta:
        verbose_name_plural = 'Parameter5FreeTime'


class Parameter6Appearance(TextModel): 

    class Meta:
        verbose_name_plural = 'Parameter6Appearance'


class Parameter7Behavior(TextModel): 

    class Meta:
        verbose_name_plural = 'Parameter7Behavior'


class Parameter8Mind(TextModel): 

    class Meta:
        verbose_name_plural = 'Parameter8Mind'
