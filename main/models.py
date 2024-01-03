from django.db import models


class SignIn(models.Model):

    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Users(models.Model):
    
    user_email = models.ForeignKey('SignIn', on_delete=models.CASCADE)
    # parameters
    
