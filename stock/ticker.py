import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime
import pandas as pd
import yfinance as yf

from django_plotly_dash import DjangoDash

app = DjangoDash('ticker')

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([html.H3('Enter stock symbols:', style={'paddingRight':'30px'}),
              dcc.Input(id='my_stock_picker',
                        value=[''],
                        multiple=True)
              ], style={'display':'inline-block','verticalAlign':'top', 'width':'30%'}),
    html.Div([html.H3('Enter normalised prices:', style={'paddingRight': '30px'}),
              dcc.Input(id='my_prices',
                        value=[''],
                        multiple=True)
              ], style={'display':'inline-block', 'verticalAlign': 'top', 'width': '30%'}),
    html.Div([html.H3('Select a start and end date:'),
              dcc.DatePickerRange(id='my_date_picker',
                                  min_date_allowed=datetime(2015,1,1),
                                  max_date_allowed=datetime.today(),
                                  start_date = datetime(2020,11,1),
                                  end_date = datetime.today()
                                  )
              ], style={'display':'inline-block'}),
    html.Div([
        html.Button(id='submit-button',
                    n_clicks=0,
                    children='Submit',
                    style={'fontSize':24, 'marginLeft':'30px'}
                    )
    ], style={'display':'inline-block'}),

    dcc.Graph(id='my_graph',
              figure={'data':[
                  {'x':[1,2], 'y':[3,1]}
              ], 'layout':{'title':'Default Title'}}
              )
])

@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('my_stock_picker', 'value'),
     State('my_prices', 'value'),
     State('my_date_picker', 'start_date'),
     State('my_date_picker', 'end_date')
     ])
def update_graph(n_clicks, stock_ticker, prices, start_date, end_date, **kwargs):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')

    traces = []
    print(stock_ticker)
    stock_info = dict(zip(stock_ticker, prices))
    print(stock_info)

    #for tic in stock_ticker:
    #       df2 = yf.download(tic, start = start, end = end)
    #       print(df2.tail())
    #       traces.append({'x': df2.index, 'y': df2['Close'], 'name': tic})

    for tic in stock_ticker:
        df2 = yf.download(tic, start = start, end = end)/stock_info[tic]
        print(df2.tail())
        traces.append({'x': df2.index, 'y': df2['Close'], 'name': tic})

    print(traces)
    fig = {
        'data':traces,
        'layout':{'title':stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()