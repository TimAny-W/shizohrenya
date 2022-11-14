from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from .forms import UserRegistrationForm


class Registration(View):
    """View class of registration new user"""

    template_name = 'registration/registration.html'

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
            return redirect('home')

        else:
            return render(request, self.template_name, context={
                'form': form,
                'errors': form.errors
            })
