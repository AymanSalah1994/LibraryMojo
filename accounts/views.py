from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'