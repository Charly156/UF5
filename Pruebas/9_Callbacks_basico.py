#Definición de librerias
import pandas as pd
import numpy as np
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

#Creación de la app de dash

app = Dash(__name__)

#Definición del layout de la app a partir de componentes HTML 
app.layout = html.Div([
    html.Label('Inserta tu respuesta en el siguiente espacio:    '),
    dcc.Input(id = 'mi-input', value = 'Valor inicial', type = 'text'),
    html.Div(id = 'mi-div'),
])

#Creación de interactividad
#Callback para actualizar texto del div en función del input mi-input
@app.callback(
    Output(component_id = 'mi-div', component_property = 'children'),
    [Input(component_id = 'mi-input', component_property = 'value')]
)
def actualizar_div(valor_entrada):
    return 'Has insertado la cadena "{}"'.format(valor_entrada)

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server(port = 8010)