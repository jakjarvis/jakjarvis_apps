from django.shortcuts import render, redirect, get_object_or_404
import json
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'worttester/home.html')

from django.shortcuts import render

