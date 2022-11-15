from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from tasks.models import Task


class CustomUser(AbstractUser):
    completed_tasks = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.completed_tasks
