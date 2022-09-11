from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Creating custom user model.


class CustomUserManager(BaseUserManager):
    # creates and saves user
    def create_user(self, first_name, last_name, email, username, password, **other_fields):
        # Validation Checks
        if not email:
            raise ValueError('A unique email address is required')
        if not username:
            raise ValueError('A unique username is required')

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name,
                          email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()

        return user
    # creates and saves super user

    def create_superuser(self, first_name, last_name, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(first_name, last_name, email, username, password, **other_fields)

    # creates and saves staff user
    def create_staffuser(self, first_name, last_name, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', False)
        other_fields.setdefault('is_active', True)

        return self.create_user(first_name, last_name, email, username, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    location = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, unique=True)
    user_image = models.TextField(blank=True)
    is_staff = models.BooleanField(default=False)
    # 👇🏽 if no secondary check (i.e email verification to activate the user) then set default to True else False
    is_active = models.BooleanField(default=True)
    # Defining that we are utilizing a new custom manager

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username
