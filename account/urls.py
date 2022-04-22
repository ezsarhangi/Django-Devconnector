from django.urls import path
from .views import create_profile,dashboard,add_experience,add_education,posts,post

urlpatterns = [
    path('create-profile', create_profile),
    path('dashboard', dashboard),
    path('add-experience', add_experience),
    path('posts',posts),
    path('post',post),
    path('add-education', add_education)
]