import random
import time

from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
from django.views import View

from .forms import UserRegistrationForm
from .models import CustomUser


class Registration(View):
    """View class of registration new user"""

    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

    def get(self, request):
        """
        Func which answers the GET request
        :return: template with context
        """
        context = {
            'form': UserRegistrationForm
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        """Func which answer the GET request
        and save new user to database
        """
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(self.success_url)

        else:
            return render(request, self.template_name, context={
                'form': form,
                'errors': form.errors
            })


class ProfileView(View):
    profile_template = 'user/profile.html'
    my_profile_template = 'user/my_profile.html'
    template_404 = 'user/404_error.html'

    def get(self, request, pk):
        try:
            user = CustomUser.objects.get(username=pk)
        except ObjectDoesNotExist:
            return render(request, self.template_404)

        context = {
            'user': user,
            'rating': self.rating()
        }

        if user == request.user and request.user.is_authenticated:
            return render(request, self.my_profile_template, context)
        else:
            return render(request, self.profile_template, context)

    def rating(self) -> list:
        """Get all states of users
        :return sorted states of users"""
        all_users = CustomUser.objects.all()
        state = []
        for user in all_users:
            state.append([user.username, user.completed_tasks.count()])
        state.sort(key=lambda x: x[1],reverse=True)
        return state

        # def sort(self, list: list) -> list:
        """Fast sorting of list
        :return sorted list
        """
        # if len(list) <= 1:
        # return list
        # else:
        # q = random.choice(list)
        # l_list = [n for n in list if n < q]

        # e_list = [q] * list.count(q)
        # b_list = [n for n in list if n > q]
        # return self.sort(l_list) + e_list + self.sort(b_list)
