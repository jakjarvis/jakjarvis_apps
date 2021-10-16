from django.shortcuts import render, redirect, get_object_or_404
from .forms import StockForm
from .models import Stock
from .models import Dividend
import stock.stock_evaluation as stock_evaluation
import json
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'stock/home.html')

@login_required
def currentstocks(request):
    stocks = Stock.objects.filter(user=request.user)

    stock_ticker = []
    stocks_list = stocks.values('ticker')
    for stock in stocks_list:
        stock_ticker += stock.values()
    unique_stocks = list(set(stock_ticker))

    return render(request, 'stock/portfolio.html',
                  {'stocks': stocks, "stock_ticker": {"my_stock_picker": {"value": unique_stocks}}})

@login_required
def portfolio(request):
        stocks = Stock.objects.filter(user=request.user)
        dividends = Dividend.objects.filter(user=request.user)
        unique_stocks = stock_evaluation.portfolio_dataframe(stocks, dividends).index.tolist()
        average_prices = stock_evaluation.portfolio_dataframe(stocks, dividends)['Av_Buy_Price_Local'].tolist()
        first_dates = stock_evaluation.portfolio_dataframe(stocks, dividends)['First_Purchase'].tolist()
        portfolio = stock_evaluation.portfolio_dataframe(stocks, dividends).reset_index().rename(columns={'index':'Ticker'})
        json_portfolio = portfolio.to_json(orient='records')
        data = []
        data = json.loads(json_portfolio)

        return render(request, 'stock/portfolio.html', {'stocks':stocks, "stock_ticker":{"my_stock_picker":{"value":unique_stocks}, "my_prices":{"value":average_prices}, "first_dates":{"value":first_dates}}, "data":data})


@login_required
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

@login_required
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

@login_required
def deletestock(request, stock_pk):
    stock = get_object_or_404(Stock, pk=stock_pk, user=request.user)
    if request.method == 'POST':
        stock.delete()
        return redirect('portfolio')

@login_required
def overview(request):
    stocks = Stock.objects.filter(user=request.user)
    dividends = Dividend.objects.filter(user=request.user)
    unique_stocks = stock_evaluation.stock_ticker(stocks)

    portfolio = stock_evaluation.portfolio_dataframe(stocks, dividends).reset_index().rename(
        columns={'index': 'Ticker'})
    json_portfolio = portfolio.to_json(orient='records')
    data = []
    data = json.loads(json_portfolio)

    return render(request, 'stock/overview.html', {'stocks':stocks, 'data':data})


