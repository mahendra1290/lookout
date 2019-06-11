from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from django.views.generic.edit import CreateView # new

from django.views.generic.edit import FormView

from .models import List

from django import forms


# Create your views here.

class HomePageView(ListView):
    model = List
    template_name = 'home.html'
    context_object_name = 'todo_list'

class AboutPageView(TemplateView):
    template_name = 'about.html'
