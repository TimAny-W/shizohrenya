from django.urls import path, include
from .views import Registration

urlpatterns = [
    path('', include('django.contrib.auth.urls'),name='home'),
    path('registration', Registration.as_view(), name='registration')

]
