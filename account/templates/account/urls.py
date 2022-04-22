from django.urls import path
from .views import create_profile,dashboard,add_experience,add_education

urlpatterns = [
    path('create-profile', create_profile),
    path('dashboard', dashboard),
    path('add-experience', add_experience),
    path('add-education', add_education)
]