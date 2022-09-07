from django.db import models

# Create your models here.


class NewUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    location = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=500)
    # user_image =
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class CustomUserManager(BaseUserManager):
    pass
