from django.db import models
from account.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=255)
    added_date = models.DateField()

    def __str__(self):
        return f"{self.title}"

    @property
    def username(self):
        return f'{str(self.user.username)}'

