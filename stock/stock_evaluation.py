import pandas as pd
from yahoo_fin import stock_info as si

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

def portfolio_dataframe(stocks):
    transactions_df = transactions_dataframe(stocks)
    index = stock_ticker(stocks)
    columns = ['Total_held', 'Av_Buy_Price', 'Total_Spent', 'Total_Return', 'Current_Value']
    portfolio_df = pd.DataFrame(index = index, columns = columns)
    for col in portfolio_df.columns:
        portfolio_df[col].values[:] = 0
    for stock in index:
        total = 0
        average = 0
        for index, row in transactions_df[transactions_df.ticker == stock].iterrows():
            if row['type'] == 'buy':
                average = ((total * average) + (row['volume'] * row['price'])) / (total + row['volume'])
                total = total + row['volume']
                portfolio_df.loc[stock, 'Total_Spent'] += row['volume'] * row['price']
            elif row['type'] == 'sel':
                total = total - row['volume']
                portfolio_df.loc[stock, 'Total_Return'] += row['volume'] * row['price']
            else:
                print('Buy/Sell not specified')
            print(total, average)
        portfolio_df.loc[stock, 'Total_held'] = total
        portfolio_df.loc[stock, 'Av_Buy_Price'] = average
        portfolio_df.loc[stock, 'Current_Value'] = round((total * si.get_live_price(stock)), 0)
    return portfolio_df