from django.urls import path
from .views import profile, profiles 

urlpatterns = [
    path('profile',profile),
    path('profiles',profiles)

]