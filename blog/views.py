from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Hello to our website!")
    return render (request,"blog/index.html",{})

def profile(request):
    return render (request,"blog/profile.html",{})

def profiles(request):
    return render (request,"blog/profiles.html",{})

