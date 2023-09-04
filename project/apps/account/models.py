from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    )
from django.utils.translation import ugettext as _


# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    pass
