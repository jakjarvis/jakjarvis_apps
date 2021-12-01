import pandas as pd
from yahoo_fin import stock_info as si
from datetime import datetime, date

def stock_ticker(stocks):
    # Returns a list of all the unique stocks that have ever been bought or sold
    ticker = []
    stocks_list = stocks.values('ticker')
    for stock in stocks_list:
        ticker += stock.values()
    unique_stocks = list(set(ticker))
    return unique_stocks

def transactions_dataframe(stocks):
    # Returns the stocks Queryset as a pandas dataframe
    df = pd.DataFrame(list(stocks.values()))
    return df

def current_holdings(stocks):
    # Returns a dictionary with the current holdings for each stock type
    holdings = {stock:0 for stock in stock_ticker(stocks)}
    df = transactions_dataframe(stocks)
    for stock in holdings:
        for index, row in df[df.ticker == stock].iterrows():
            if row['type'] == 'buy':
                holdings[stock] += row.volume
            elif row['type'] == 'sel':
                holdings[stock] -= row.volume
            else:
                print('Buy/Sell not specified')
    return holdings

def portfolio_dataframe(stocks, dividends):
    transactions_df = transactions_dataframe(stocks)
    dividends_df = transactions_dataframe(dividends)
    index = stock_ticker(stocks)
    columns = ['Total_held', 'Av_Buy_Price', 'Total_Spent', 'Total_Return', 'Current_Value', 'First_Purchase']
    portfolio_df = pd.DataFrame(index = index, columns = columns)
    for col in portfolio_df.columns:
        portfolio_df[col].values[:] = 0
    for stock in index:
        total = 0
        average_local = 0
        average = 0
        date = datetime.today().date()
        returned = 0
        spent = 0
        for index, row in transactions_df[transactions_df.ticker == stock].iterrows():
            if row['type'] == 'buy':
                average_local = ((total * average_local) + (row['volume'] * row['price'])) / (total + row['volume'])
                average = ((total * average) + (row['volume'] * row['price'] / row['currency_con'])) / (total + row['volume'])
                total = total + row['volume']
                spent += row['volume'] * row['price'] / row['currency_con']
                if row['date'] <= date:
                    date = row['date']
            elif row['type'] == 'sel':
                total = total - row['volume']
                returned += row['volume'] * row['price'] / row['currency_con']
            else:
                print('Buy/Sell not specified')
            currency = row['currency']
        for index, row in dividends_df[dividends_df.ticker == stock].iterrows():
            returned += row['value'] / row['currency_con']
        if(currency == 'EUR'):
            value_now = round((total * si.get_live_price(stock)), 0)
        else:
            value_now = round((total * si.get_live_price(stock)), 0) / si.get_live_price(currency)
        portfolio_df.loc[stock, 'Total_held'] = round(total, 2)
        portfolio_df.loc[stock, 'Total_Spent'] = round(spent, 2)
        portfolio_df.loc[stock, 'Total_Return'] = round(returned, 2)
        portfolio_df.loc[stock, 'Av_Buy_Price_Local'] = round(average_local, 2)
        portfolio_df.loc[stock, 'Av_Buy_Price'] = round(average, 2)
        portfolio_df.loc[stock, 'First_Purchase'] = date
        portfolio_df.loc[stock, 'Current_Value'] = round(value_now, 2)
        portfolio_df.loc[stock, 'Total_PL'] = round((value_now + returned - spent), 2)
        portfolio_df.loc[stock, 'Gain'] = round(portfolio_df.loc[stock, 'Total_PL'] / portfolio_df.loc[stock, 'Total_Spent'], 3) * 100
    portfolio_df.loc['Total', 'Total_Spent'] = portfolio_df['Total_Spent'].sum()
    portfolio_df.loc['Total', 'Total_Return'] = portfolio_df['Total_Return'].sum()
    portfolio_df.loc['Total', 'Current_Value'] = portfolio_df['Current_Value'].sum()
    portfolio_df.loc['Total', 'Total_PL'] = portfolio_df['Total_PL'].sum()
    portfolio_df.loc['Total', 'Gain'] = round(portfolio_df['Total_PL'].sum() / portfolio_df['Total_Spent'].sum(), 3) * 100
    portfolio_df.fillna("",inplace=True)
    return portfolio_df