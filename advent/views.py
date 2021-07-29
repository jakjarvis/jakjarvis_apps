from django.shortcuts import render
from .models import Advent

def home(request):
    puzzles = Advent.objects.all()
    return render(request, 'advent/home.html')