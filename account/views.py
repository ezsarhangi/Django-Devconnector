from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_profile(request):
    return render(request,'account/create-profile.html',{})

def dashboard(request):
    return render(request,'account/dashboard.html',{})

def add_experience(request):
    return render(request,'account/add-experience.html',{})

def add_education(request):
    return render(request,'account/add-education.html',{})

def posts(request):
    return render (request,"account/posts.html",{})

def post(request):
    return render (request,"account/post.html",{})