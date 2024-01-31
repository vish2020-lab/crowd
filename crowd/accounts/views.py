from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import auth, User

from django.http import HttpResponse
from .models import crowduser

# Create your views here.


def register(request):
    if request.method=='POST':
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']

    else:
        return render(request, 'register.html')
    
