#Definición de librerías
from dash import Dash, html, dcc
import pandas as pd
from dash.dependencies import Input, Output #Módulos de interactividad Input, Output
import plotly.graph_objs as go

app = Dash(__name__)

#Carga de datos
df = pd.read_excel(r'D:\Tecnologico de Monterrey\Clases\Semestre 7\Analitica II\UF5\Pruebas\Info_pais.xlsx')

variables = df.columns #Lista con las columnas del dataframe que estarán en los dropdowns

#Definición del layout de la app a partir de componentes HTML y Core
app.layout = html.Div([
                html.Div([
                dcc.Dropdown(
                    id='ejex',
                    options=[{'label': i, 'value': i} for i in variables],
                    value='Renta per capita'
                    )
                    ],style={'width': '48%','display': 'inline-block'}),

                html.Div([
                dcc.Dropdown(
                    id='ejey',
                    options=[{'label': i, 'value': i} for i in variables],
                    value='Esperanza de vida'
                    )
                    ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

                dcc.Graph(id='grafico_var')
], style={'padding':10})

# CREACIÓN DE GRÁFICOS E INTERACTIVIDAD
#Callback para actualizar gráfico en función de los 2 dropdowns
@app.callback(
    Output('grafico_var', 'figure'),
    [Input('ejex', 'value'), Input('ejey', 'value')])
def actualizar_graf(nombre_ejex, nombre_ejey):
    return {
        'data': [go.Scatter(
            x=df[nombre_ejex], #la selección realizada en el primer dropdown
            y=df[nombre_ejey], #la selección realizada en el segundo dropdown
            text=df['País'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={'title': nombre_ejex, 'tickangle': 45},
            yaxis={'title': nombre_ejey},
            margin={'l': 40, 'b': 80, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server()
