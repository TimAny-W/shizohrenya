from django.contrib import admin
from .models import Task, TaskGroup

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'creating_date')


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskGroup)