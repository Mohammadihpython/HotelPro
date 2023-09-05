from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _

from .manager import CustomUserManager

phone_regex = RegexValidator(
    regex=r"^\+{1}989\d{9}$",
    message="Phone number must be entered in the format: "
    "'+989xxxxxxxxx'. Up to 14 digits allowed.",
)


# Create your models here.
class CustomUser(AbstractUser, PermissionsMixin):
    phone_number = models.CharField(
        _("Phone number"), max_length=11, unique=True, validators=[phone_regex]
    )

    USERNAME_FIELD = "phone_number"

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number
