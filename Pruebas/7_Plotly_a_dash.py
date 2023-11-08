#Importación de librerías
from dash import Dash, html, dcc
import plotly.graph_objs as go
import pandas as pd

#Creación de la app de dash
app = Dash(__name__)

# Carga datos
df_iris = pd.read_csv(r'D:\Rigo\Rigo\Documentacion Tec Monterrey\Semestre Agosto-Diciembre\Analítica de datos y herramientas de IA II\Dash\iris_dataset.csv',encoding = 'ISO-8859-1',delimiter=',')

#Objetos plotly.graph
data1 = [go.Scatter(x=df_iris["longitud_sépalo"],
                    y=df_iris["anchura_sépalo"],
                    mode="markers",
                    marker = dict(
                            size=12,
                            symbol="circle",
                            line={"width":3} #línea del marcador
                    ))]

layout1 = go.Layout(title="Iris Scatter plot sépalo",
                    xaxis=dict(title="Longitud sépalo"),
                    yaxis=dict(title="Anchura sépalo"))

'''
data2 = [go.Scatter(x=df_iris["longitud_pétalo"],
                    y=df_iris["anchura_pétalo"],
                    mode="markers",
                    marker = dict(
                            size=12,
                            symbol="hexagon-dot",
                            line={"width":1}, #línea del marcador
                            color= 'cyan'
                    ))]

layout2 = go.Layout(title="Iris Scatter plot pétalo",
                    xaxis=dict(title="Longitud pétalo"),
                    yaxis=dict(title="Anchura pétalo"),
                    font=dict(color="darkmagenta"),
                    paper_bgcolor="indigo")'''


#Definición del layout de la app a partir de componentes HTML y Core
app.layout = html.Div([
                dcc.Graph(id='scatterplot',
                    figure = {'data':data1,
                            'layout':layout1}
                    ),
#                    dcc.Graph(id='scatterplot2',
#                    figure = {'data':data2,
#                            'layout':layout2}
#                              )
                    ])

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    #app.run_server(port=8000)
    app.run_server()
