from django.shortcuts import render  ,redirect
from django.urls import reverse_lazy 
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    # success_url = redirect('login')
    def get_success_url(self) -> str:
        return reverse_lazy('login')