from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import TaskCreateForm, TaskGroupCreateForm
from .models import Task

from django.contrib.auth.mixins import LoginRequiredMixin


# from user_system.models import CustomUser


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task.html'


class TaskCreate(LoginRequiredMixin, View):
    """Class for create task"""
    template_name = 'tasks/task_form.html'

    def get(self, request):
        """Func which answer the GET method
        return template with task form
        """

        return render(request,
                      self.template_name,
                      context={
                          "form": TaskCreateForm
                      }
                      )

    def post(self, request):
        """Func which answer the POST method

        if form valid: get and save the form
        else: return form and errors
        """
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            commit = form.save(commit=False)
            commit.user = request.user
            commit.save()
            return redirect('tasks')
        else:
            context = {'form': form,
                       'errors': form.errors}
            return render(request, self.template_name, context)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


class TaskComplete(LoginRequiredMixin, View):
    template_name = 'tasks/task_confirm_complete.html'

    def get(self, request, pk):
        """Answer GET method
        return template with current task context"""
        context = {
            'task': Task.objects.get(id=pk)
        }
        return render(request, self.template_name, context=context)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.is_completed = True
        task.save()
        request.user.completed_tasks.add(task)
        print(f'{task.title} is switched to {task.is_completed}')
        return redirect('tasks')


class TaskListCompleted(LoginRequiredMixin, View):
    template_name = 'tasks/task_list_completed.html'

    def get(self, request):
        context = {
            'list': request.user.completed_tasks.all()
        }
        return render(request, self.template_name, context)


class TaskGroupCreate(LoginRequiredMixin, View):
    template_name = 'tasks/task_group_create.html'

    def get(self, request):
        context = {
            'form': TaskGroupCreateForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = TaskGroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                'form': form,
                'errors': form.errors
            }
            return render(request, self.template_name)
