from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'creating_date')


admin.site.register(Task, TaskAdmin)