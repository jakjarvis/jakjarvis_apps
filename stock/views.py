from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import StockForm
from .models import Stock
from django_plotly_dash.consumers import send_to_pipe_channel

def home(request):
    return render(request, 'stock/home.html')

def signupuser(request):
    if request.method == "GET":
        return render(request, 'stock/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], 'na', request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentstocks')
            except IntegrityError:
                return render(request, 'stock/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'That Username is taken - try a new one.'})
        else:
            return render(request, 'stock/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def currentstocks(request):
    stocks = Stock.objects.filter(user=request.user)

    stock_ticker = []
    stocks_list = stocks.values('ticker')
    for stock in stocks_list:
        stock_ticker += stock.values()
    print(stock_ticker)

    return render(request, 'stock/current.html', {'stocks':stocks, 'stock_ticker':stock_ticker})

def loginuser(request):
    if request.method == "GET":
        return render(request, 'stock/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'stock/loginuser.html', {'form': AuthenticationForm(), 'error':'Username and Password did not match'})
        else:
            login(request, user)
            return redirect('currentstocks')

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

def createstock(request):
    if request.method == "GET":
        return render(request, 'stock/createstock.html', {'form': StockForm()})
    else:
        try:
            form = StockForm(request.POST)
            newstock = form.save(commit=False)
            newstock.user = request.user
            newstock.save()
            return redirect('currentstocks')
        except ValueError:
            return render(request, 'stock/createstock.html', {'form': StockForm(), 'error':'Bad data passed in'})

def viewstock(request, stock_pk):
    stock = get_object_or_404(Stock, pk=stock_pk, user=request.user)
    if request.method == 'GET':
        form = StockForm(instance=stock)
        return render(request, 'stock/viewstock.html', {'stock': stock, 'form': form})
    else:
        try:
            form = StockForm(request.POST, instance=stock)
            form.save()
            return redirect('currentstocks')
        except ValueError:
            return render(request, 'todo/viewstock.html', {'stock': stock, 'form': form, 'error': 'Bad Info'})

def deletestock(request, stock_pk):
    stock = get_object_or_404(Stock, pk=stock_pk, user=request.user)
    if request.method == 'POST':
        stock.delete()
        return redirect('currentstocks')
