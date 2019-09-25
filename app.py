#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 00:50:11 2019

@author: apple
"""

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')


markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

colors = {
        'background': '#111111',
        'text': '#7FDBFF'       
        }

app.layout = html.Div(children=[ 
        
        html.H1('Live Chat',style={'textAlign':'center','color':colors['text']}),
        
        html.Div('Customer Chat Analysis',style={'textAlign':'center','color':colors['text']}),

#Bar plot        
        dcc.Graph(
                id='live-graph',
                figure={
                        'data':[
                                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                                ],
                        'layout':{
                                'title':'Live Chat Plot',
                                 'plot_bgcolor': colors['background'],
                                 'paper_bgcolor': colors['background'],
                                 'font': {'color': colors['text']}
                                }
                        
                        }
                
                ),

#Scatter Plot
     
        dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
                        )
                    }
                ),


        
        html.Div([
        html.Label('Dropdown'),
        dcc.Dropdown(
                options=[
                         {'label': 'New York City', 'value': 'NYC'},
                         {'label': u'Montréal', 'value': 'MTL'},
                         {'label': 'San Francisco', 'value': 'SF'}
                        ],
                        value='MTL'
                    ),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value=['MTL', 'SF'],
            multi=True
        ),
        
        html.Label('Radio Items'),
        dcc.RadioItems(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL'
        ),
        
          html.Label('Checkboxes'),
          dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    ),
            
          html.Label('Text Input'),
          dcc.Input(value='MTL', type='text'),
          
        html.Label('Slider'),
        dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=5,
        )
        
        ],
          style={'columnCount': 2} 
         ),
                

 html.Div(
 dcc.Markdown(children=markdown_text),
)
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
