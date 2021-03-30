# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:40:30 2021

@author: mpenm
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import date
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
      
    html.H4(children='Enter your Trade Idea: '),
    html.Br(),
    html.Div([
    html.Div([
        html.Label('Enter Ticker Symbol'),
        dcc.Input(id = 'ticker-input', value='', type='text'),
        html.Br(),
        html.Br(),
        html.Div([html.Label('Select risk'),
                  dcc.RadioItems(id = 'risk', options=[{'label': 'Low', 'value': 'low'},
                                                       {'label': 'Medium', 'value': 'medium'},
                                                       {'label': 'High', 'value': 'high'}], value='low' )]),
        html.Br(),
        html.Div([html.Label('Select trade type'),
                  dcc.RadioItems(id = 'trade-type', options=[{'label': 'call', 'value': 'call'},
                                                             {'label': 'put', 'value': 'put'},
                                                             {'label': 'share', 'value': 'share'},
                                                             {'label': 'other', 'value': 'other'}], value='call' )]), html.Br()]),
    html.Label('If other - specify in trade rationale section'),
    html.Br(),
    html.Button('verify', id='button1', n_clicks=0),
    html.Br(),
    html.Br(),
    html.Label('Select expiry for option'),
    dcc.DatePickerSingle(id='date-picker', date=date.today()),
    html.Br(),
        html.Label('Enter Strike price'),
        dcc.Input(id = 'strike-input', value='', type='number'),
        html.Br(),
    html.Label('Enter Trade Rationale'),dcc.Textarea(id='trade-rationale', style={'width': '75%', 'height': 300})], style={'columnCount': 2}),
    html.H3(children='Confirm Trade Idea: '),
        html.Div([html.Label('Ticker:',style={'display': 'inline-block'}),html.Div(id ='ticker-output',style={"margin-left": "15px",'display': 'inline-block'})]),
    html.Div([html.Label('Risk:',style={'display': 'inline-block'}),html.Div(id ='risk-output',style={"margin-left": "15px",'display': 'inline-block'})]),
    html.Div([html.Label('Trade type:',style={'display': 'inline-block'}),html.Div(id ='ttype-output',style={"margin-left": "15px",'display': 'inline-block'})]),
    html.Div([html.Label('Expiry:',style={'display': 'inline-block'}),html.Div(id ='date-output',style={"margin-left": "15px",'display': 'inline-block'})]),
    html.Div([html.Label('Strike:',style={'display': 'inline-block'}),html.Div(id ='strike-output',style={"margin-left": "15px",'display': 'inline-block'})]),
    html.Div([html.Label('Rationale:',style={'display': 'inline-block'}),html.Div(id ='rationale-output',style={"margin-left": "15px",'display': 'inline-block'})]),
    html.Br(),
    html.Br(),
    html.Button('Submit', id='button2', n_clicks=0),
    html.Div(id='json-output')
    
    
    ])

    
@app.callback(
                  [Output('ticker-output', 'children'),
                  Output('risk-output', 'children'),
                  Output('ttype-output', 'children'),
                  Output('date-output', 'children'),
                  Output('strike-output', 'children'),
                  Output('rationale-output', 'children')],
                  [Input('ticker-input', 'value'),
                  Input('risk', 'value'),
                  Input('trade-type', 'value'),
                  Input('date-picker', 'date'),
                  Input('strike-input', 'value'),
                  Input('trade-rationale', 'value'),
                  Input('button1', 'n_clicks')]
                )

def update_output_div(ticker,risk,tradetype,date,strike,trade_rationale,n_clicks):
    
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

    if 'button1' in changed_id:
        return ticker,risk,tradetype,date,strike,trade_rationale
        
    else:
        return '','','','','',''
    
@app.callback(
                  Output('json-output', 'children'),
                  [Input('ticker-input', 'value'),
                  Input('risk', 'value'),
                  Input('trade-type', 'value'),
                  Input('date-picker', 'date'),
                  Input('strike-input', 'value'),
                  Input('trade-rationale', 'value'),
                  Input('button2', 'n_clicks')]
                )

def update_output_json(ticker,risk,tradetype,date,strike,trade_rationale,n_clicks):
    
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

    if 'button2' in changed_id:
        data= {'ticker': ticker,
               'risk': risk,
               'tradetype': tradetype,
               'date': date,
               'strike': strike,
               'trade_rationale': trade_rationale}
        json_data = json.dumps(data)
        return json_data
        
    else:
        return ''
if __name__ == '__main__':
    app.run_server(debug=True)