from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def lmao(request):
    return HttpResponse("<em>Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It is free and open source, has a thriving and active community, great documentation, and many options for free and paid-for support.</em>")