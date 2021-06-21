from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Project
from django.contrib.auth.decorators import login_required

def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects':projects})

def signupuser(request):
    if request.method == "GET":
        return render(request, 'projects/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], 'na', request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'projects/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'That Username is taken - try a new one.'})
        else:
            return render(request, 'projects/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == "GET":
        return render(request, 'projects/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'projects/loginuser.html', {'form': AuthenticationForm(), 'error':'Username and Password did not match'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
