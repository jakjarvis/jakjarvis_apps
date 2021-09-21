import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import date, datetime
import pandas as pd
import yfinance as yf

from django_plotly_dash import DjangoDash

app = DjangoDash('ticker')

app.layout = html.Div([
    html.Div([html.H3('Stock symbols:', style={'paddingRight':'30px'}),
              dcc.Input(id='my_stock_picker',
                        value=[''],
                        multiple=True)
              ], style={'display':'none','verticalAlign':'top', 'width':'30%'}),
    html.Div([html.H3('Normalised prices:', style={'paddingRight': '30px'}),
              dcc.Input(id='my_prices',
                        value=[''],
                        multiple=True)
              ], style={'display':'none', 'verticalAlign': 'top', 'width': '30%'}),
    html.Div([html.H3('First Purchase Date:', style={'paddingRight': '30px'}),
              dcc.Input(id='first_dates',
                        value=[''],
                        multiple=True)
              ], style={'display':'none', 'verticalAlign': 'top', 'width': '30%'}),
    dcc.Graph(id='my_graph',
              figure={'data':[
                  {'x':[1,2], 'y':[3,1]}
              ], 'layout':{'title':'Default Title'}}
              )
])

@app.callback(
    Output('my_graph', 'figure'),
    [Input('my_stock_picker', 'value'),
     Input('my_prices', 'value'),
     Input('first_dates', 'value')
     ])

def update_graph(stock_ticker, prices, first_date, **kwargs):
    end = datetime.today().date()

    traces = []
    stock_prices = dict(zip(stock_ticker, prices))
    stock_dates = dict(zip(stock_ticker, first_date))

    print(stock_dates)

    #for tic in stock_ticker:
    #       df2 = yf.download(tic, start = start, end = end)
    #       print(df2.tail())
    #       traces.append({'x': df2.index, 'y': df2['Close'], 'name': tic})

    for tic in stock_ticker:
        print(stock_dates[tic])
        df2 = yf.download(tic, start = stock_dates[tic], end = end)/stock_prices[tic]
        traces.append({'x': df2.index, 'y': df2['Close'], 'name': tic})

    fig = {
        'data':traces,
        'layout':{'title':'Stock ticker'}
    }
    return fig

if __name__ == '__main__':
    app.run_server()