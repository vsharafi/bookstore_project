from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/accounts/login'


