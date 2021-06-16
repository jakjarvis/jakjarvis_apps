from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import StockForm
from .models import Stock
import stock.stock_evaluation as stock_evaluation
import json
import pandas as pd

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
                return redirect('portfolio')
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
    unique_stocks = list(set(stock_ticker))

    return render(request, 'stock/portfolio.html',
                  {'stocks': stocks, "stock_ticker": {"my_stock_picker": {"value": unique_stocks}}})

def portfolio(request):
    stocks = Stock.objects.filter(user=request.user)
    #unique_stocks = stock_evaluation.stock_ticker(stocks)
    unique_stocks = stock_evaluation.portfolio_dataframe(stocks).index.tolist()
    average_prices = stock_evaluation.portfolio_dataframe(stocks)['Av_Buy_Price'].tolist()

    portfolio = stock_evaluation.portfolio_dataframe(stocks).reset_index().rename(columns={'index':'Ticker'})
    print(portfolio)
    json_portfolio = portfolio.to_json(orient='records')
    data = []
    data = json.loads(json_portfolio)

    return render(request, 'stock/portfolio.html', {'stocks':stocks, "stock_ticker":{"my_stock_picker":{"value":unique_stocks}, "my_prices":{"value":average_prices}}, "data":data})

def loginuser(request):
    if request.method == "GET":
        return render(request, 'stock/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'stock/loginuser.html', {'form': AuthenticationForm(), 'error':'Username and Password did not match'})
        else:
            login(request, user)
            return redirect('portfolio')

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
            return redirect('portfolio')
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
            return redirect('portfolio')
        except ValueError:
            return render(request, 'todo/viewstock.html', {'stock': stock, 'form': form, 'error': 'Bad Info'})

def deletestock(request, stock_pk):
    stock = get_object_or_404(Stock, pk=stock_pk, user=request.user)
    if request.method == 'POST':
        stock.delete()
        return redirect('portfolio')

def overview(request):
    stocks = Stock.objects.filter(user=request.user)
    unique_stocks = stock_evaluation.stock_ticker(stocks)

    portfolio = stock_evaluation.portfolio_dataframe(stocks).reset_index().rename(columns={'index':'Ticker'})
    print(portfolio)
    json_portfolio = portfolio.to_json(orient='records')
    data = []
    data = json.loads(json_portfolio)

    transactions = stock_evaluation.transactions_dataframe(stocks)
    holdings = stock_evaluation.current_holdings(stocks)

    return render(request, 'stock/overview.html', {'stocks':stocks, 'data':data})


