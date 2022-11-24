from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from tasks.models import Task


class CustomUser(AbstractUser):
    avatar = models.ImageField('Аватарка', default='', upload_to=f'user_avatars')

    completed_tasks = models.ManyToManyField(Task, )

    def __str__(self):
        return self.username
