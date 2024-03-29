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
    """Registration of new user"""

    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

    def get(self, request):
        """return template with User Registration form"""
        context = {
            'form': UserRegistrationForm
        }

        return render(request,
                      self.template_name,
                      context)

    def post(self, request):
        """Save new user to database"""
        print(request.FILES)
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data.get('avatar'))
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect(self.success_url)

        else:
            return render(request,
                          self.template_name,
                          context={
                              'form': form,
                              'errors': form.errors
                          }
                          )


class ProfileView(View):
    """return a html of profile """

    profile_template = 'user/profile.html'
    my_profile_template = 'user/my_profile.html'
    template_404 = 'user/404_error.html'

    def get(self, request, pk):
        """Return a html of profile"""

        try:
            user = CustomUser.objects.get(username=pk)

        except ObjectDoesNotExist:
            return render(request, self.template_404)

        rating_list,user_place = self.rating()
        context = {
            'user': user,
            'rating': rating_list,
            'place_user': user_place
        }

        if user == request.user and request.user.is_authenticated:

            return render(request,
                          self.my_profile_template,
                          context)

        else:
            return render(request,
                          self.profile_template,
                          context)

    def rating(self):
        """Get all states of users
        :return sorted states of users"""

        all_users = CustomUser.objects.all()
        user_place = ''
        state = []

        for user in all_users:
            state.append([user.username, user.completed_tasks.count()])

        state.sort(key=lambda x: x[1], reverse=True)

        for place in range(len(state)):  # Берем длину списка,и перебираем эту длину,вписываем как место в рейтинге
            state[place].append(place + 1)

        for user in state:
            if user[0] == self.request.user:
                print('gay')
                user_place = user[2]
        return state, user_place

        # def sort(self, list: list) -> list:
        # if len(list) <= 1:
        # return list
        # else:
        # q = random.choice(list)
        # l_list = [n for n in list if n < q]

        # e_list = [q] * list.count(q)
        # b_list = [n for n in list if n > q]
        # return self.sort(l_list) + e_list + self.sort(b_list)
