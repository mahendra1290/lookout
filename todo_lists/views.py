from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from django.views.generic.edit import CreateView # new

from django.views.generic.edit import FormView

from .models import List, User

from django import forms

from .forms import UserLoginForm
# Create your views here.

class HomePageView(ListView):
    model = List
    template_name = 'home.html'
    context_object_name = 'todo_list'

class LoginPageView(FormView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = '/home/'

class SignupPageView(CreateView):
    username = forms.CharField(label='')
    class Meta:
        model = User
        template_name = 'signup.html'
        fields = ['username']
        success_url = '/home/'

class AboutPageView(TemplateView):
    template_name = 'about.html'
