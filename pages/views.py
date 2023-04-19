from django.shortcuts import render
from django.views.generic import TemplateView

""" 
TemplateView is a useful tool for rendering
templates in Django and is suitable for simple
use cases where data processing is not required.
"""


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
