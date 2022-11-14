from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import TaskCreateForm
from .models import Task

from django.contrib.auth.mixins import LoginRequiredMixin


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
        """Func which answer the GET method"""
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
            return render(request,self.template_name,context)



class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
