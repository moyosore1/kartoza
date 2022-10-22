from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name="date joined"
    )
    last_login = models.DateTimeField(auto_now=True, verbose_name="last login")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15)
    home_address = models.CharField(max_length=70)
    longitude = models.DecimalField(max_digits=5, decimal_places=7)
    latitude = models.DecimalField(max_digits=5, decimal_places=7)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number", "home_address", "longitude", "latitude"]
