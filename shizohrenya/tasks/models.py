from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('Название', max_length=30)
    text = models.TextField('Текст', max_length=255)
    complete = models.BooleanField('Выполнение', default=False)
    creating_date = models.DateTimeField('Дата', null=True, auto_now_add=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['complete', 'creating_date']