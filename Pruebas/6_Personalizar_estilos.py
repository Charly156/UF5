import pandas as pd
import numpy as np

from dash import Dash, html, dcc

#Creación de la app de dash

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

#Definición del layout de la app a partir de componentes HTML 
app.layout = html.Div([
    html.H1(children = 'Primer Dashboard con Dash',
            style = {
                'textAlign': 'center',
                'color': colors['text']
            }),
    html.Div(children = 'Dash es un Framework para aplicaciones web',
            style = {
                'textAlign': 'center',
                'color': colors['text']
            }),
    dcc.Graph(id = 'Figura_inicial',
              figure = {
                  'data':[
                      {'x':[1,2,3,6,8], 'y':[6,8,3,10,4], 'type': 'bar', 'name': 'Puebla'},
                      {'x':[5,3,4], 'y':[3,6,9], 'type': 'bar', 'name': 'México'},
                  ],
                  'layout':{'title':'Comparativa Puebla-México',
                            'plot_bgcolor': colors['background'],
                            'paper_bgcolor': colors['background'],
                            'font': {'color': colors['text']}}
              })
])

style = {'backgroundColor':colors['background']}

if __name__ == '__main__':
    app.run(port = 8000)