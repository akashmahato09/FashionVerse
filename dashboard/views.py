from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def myprofile(request):
    
    return render(request, "dashboard/myprofile.html")