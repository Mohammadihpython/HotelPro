from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime
from datetime import timedelta
from .manager import CustomUserManager
from django.utils import timezone


phone_regex = RegexValidator(
    regex=r"^09\d{9}$",
    message="Phone number must be entered in the format: "
    "'09xxxxxxxxx'. Up to 11 digits allowed.",
)


# Create your models here.
class CustomUser(AbstractUser, PermissionsMixin):
    phone_number = models.CharField(
        _("Phone number"), max_length=14, unique=True, validators=[phone_regex]
    )
    verify = models.BooleanField(_("verify"), default=False)

    USERNAME_FIELD = "phone_number"

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number


def default_expire_time():
    return timezone.make_aware(datetime.now() + timedelta(minutes=5))


class OTPRequestQuertSet(models.QuerySet):
    def is_valid(self, phone_number, code):
        current_time = timezone.now()
        result = self.filter(
            phone_number=phone_number,
            code=code,
            expire_time_start__lt=current_time,
            expire_time_end__gt=current_time,
        ).exists()
        return result


class OTPManager(models.Manager):
    def get_queryset(self):
        return OTPRequestQuertSet(self.model, using=self._db)

    def is_valid(self, phone_number, code):
        return self.get_queryset().is_valid(phone_number, code)

    def generate(self, data):
        user_otp = self.model(
            phone_number=data["phone_number"],
            code=data["code"],
        )
        user_otp.save(using=self._db)
        return user_otp


class UserOTP(models.Model):
    SIGNUP = 1
    LOGIN = 2
    EMAIL = 3
    CODE_TYPE_CHOICE = (
        (SIGNUP, _("sing up")),
        (LOGIN, _("LOGIN")),
        (EMAIL, _("email")),
    )

    code = models.CharField(verbose_name=_("code"), max_length=6)
    expire_time_start = models.DateTimeField(
        verbose_name=_("start of expire time"),
        auto_now_add=True,
        null=True,
        blank=True,
    )
    expire_time_end = models.DateTimeField(
        _("end of expire time"), default=default_expire_time, null=True, blank=True
    )
    code_type = models.IntegerField(
        _("code type"), choices=CODE_TYPE_CHOICE, null=True, default=1
    )
    phone_number = models.CharField(
        _("Phone number"),
        max_length=14,
        validators=[phone_regex],
        null=True,
        blank=True,
    )

    objects = OTPManager()
