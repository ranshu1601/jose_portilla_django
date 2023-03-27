from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def lmao(request):
    my_dict = {'insert_me':'hello i am from view.py !!!'}
    return render(request,"AppTwo\index.html",context=my_dict)