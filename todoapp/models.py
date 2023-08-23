from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=255)
    added_date = models.DateField()
