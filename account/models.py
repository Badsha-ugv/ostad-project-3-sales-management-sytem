from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, db_index=True,  on_delete= models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.username} profile'


class LoginOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.user.username} opt'