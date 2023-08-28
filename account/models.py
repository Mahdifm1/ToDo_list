from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
