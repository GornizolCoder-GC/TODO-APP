from django.db import models

# Create your models here.
from django.utils import timezone


class TodoApp(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title