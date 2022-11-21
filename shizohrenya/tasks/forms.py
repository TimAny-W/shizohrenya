from django.forms import ModelForm
from .models import Task


class TaskCreateForm(ModelForm):
    """Task create form"""

    class Meta:
        model = Task
        fields = ['title', 'text', 'complete_date', ]
