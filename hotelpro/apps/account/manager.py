from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    use_in_migrations = True
    
    def _create_user(self,phone_number,password,**extra_fields):
        if not phone_number:
            raise ValueError(_('Please enter a phone number'))
        
        user = self.model(phone_number=phone_number,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)
    
    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone_number, password, **extra_fields)
    