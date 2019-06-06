from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from django.views.generic.edit import CreateView # new

from .models import List, User

# Create your views here.

class HomePageView(ListView):
    model = List
    template_name = 'home.html'
    context_object_name = 'todo_list'

class LoginPageView(CreateView):
    model = User
    template_name = 'login.html'
    fields = '__all__'

class AboutPageView(TemplateView):
    template_name = 'about.html'
