from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    added_date = models.DateField()
