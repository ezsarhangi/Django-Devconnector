from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render (request,"authentication/login.html",{})

def register(request):
    return render (request,"authentication/register.html",{})