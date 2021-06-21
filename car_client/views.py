from django.shortcuts import render
from .client import launch_client
from django.contrib.auth.decorators import login_required

@login_required
def launcher(request):
    launch_client()
    return render(request, 'car_client/launcher.html')


