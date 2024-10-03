from django.contrib import admin
from django.contrib.auth.models import User 

from .models import UserProfile, LoginOTP

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    pass 


admin.site.register(LoginOTP)