from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('Название', max_length=30)
    text = models.TextField('Текст', max_length=255)
    complete = models.BooleanField('Выполнение', default=False)
    creating_date = models.DateTimeField('Дата', null=True, auto_now=True)
    complete_date = models.DateTimeField('Дата выполненения', null=True)
    is_completed = models.BooleanField("Выполнена ли задача?", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['complete', 'creating_date']


class TaskGroup(models.Model):
    group_name = models.CharField(max_length=20)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.group_name
