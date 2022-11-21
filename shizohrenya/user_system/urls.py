from django.urls import path, include
from .views import Registration, ProfileView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('registration', Registration.as_view(), name='registration'),

    path('profile/<str:pk>', ProfileView.as_view(),name='profile')
]
