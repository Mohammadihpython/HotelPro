from django.contrib import admin

# Register your models here.
from .models import CustomUser, UserOTP

admin.site.register(CustomUser)
admin.site.register(UserOTP)
