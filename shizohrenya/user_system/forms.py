from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import models

user = get_user_model()


class UserRegistrationForm(UserCreationForm):
    """Class of form registration new user"""

    class Meta:
        model = user
        fields = ['username', 'email', ]
