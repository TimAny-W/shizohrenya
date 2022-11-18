# Generated by Django 4.0.6 on 2022-11-18 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('text', models.TextField(max_length=255, verbose_name='Текст')),
                ('complete', models.BooleanField(default=False, verbose_name='Выполнение')),
                ('creating_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата')),
                ('complete_date', models.DateTimeField(null=True, verbose_name='Дата выполненения')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Выполнена ли задача?')),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
                'ordering': ['complete', 'creating_date'],
            },
        ),
    ]
