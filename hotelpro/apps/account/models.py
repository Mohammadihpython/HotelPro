from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    AbstractUser
    )
from django.utils.translation import gettext as _
from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser,PermissionsMixin):
    phone_number = models.CharField(max_length=11,unique=True)
    
    USERNAME_FIELD = ("phone_number")
    
    objects = CustomUserManager()
    
    
    def __str__(self):
        return self.phone_number
    
