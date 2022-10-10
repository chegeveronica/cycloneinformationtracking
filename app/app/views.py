from django.shortcuts import render
from django.views import generic
from core.models import Cyclone_info # bring News into the views

# Create your views here.

class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'articles'
     
    def get_queryset(self):
        return Cyclone_info.objects.all()