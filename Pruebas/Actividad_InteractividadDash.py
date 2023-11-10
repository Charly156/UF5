#Importación de librerías
from dash import Dash, html, dcc
import plotly.graph_objs as go
import pandas as pd

#Creación de la app de dash
app = Dash(__name__)

# Carga datos
df_iris = pd.read_csv(r'D:\Tecnologico de Monterrey\Clases\Semestre 7\Analitica II\UF5\Pruebas\SP500_data_.csv',encoding = 'ISO-8859-1',delimiter=',')

data1 = [go.Scatter(x=df_iris["Date"],
                    y=df_iris["Close"],
                    mode="lines",
                    marker = dict(
                            size=12,
                            symbol="circle",
                            line={"width":3} #línea del marcador
                    ))]

layout1 = go.Layout(title="Gráfico de línea con Close",
                    xaxis=dict(title="Años"),
                    yaxis=dict(title="Close"))

data2 = [{
    "x": df_iris["Date"],
    "y": df_iris["Volume"],
    "type": "bar",
    "marker": {
        "size": 12,
        "symbol": "circle",
        "line": {"width": 3}  # línea del marcador
    }
}]

layout2 = go.Layout(title="Gráfico de barras con Volume",
                    xaxis=dict(title="Años"),
                    yaxis=dict(title="Volumen"))

app.layout = html.Div([
    dcc.Dropdown(
        options = [
            {'label': 'Valor a la apertura', 'value': 'Open'},
            {'label': 'Valor al cierre', 'value': 'Close'}
        ],

        value = 'Open' 
    ),
    dcc.Graph(id='line',
              figure = {'data':data1,
                        'layout':layout1}
    ),
    dcc.Graph(id='bar',
              figure = {'data':data2,
                        'layout':layout2}
    )
])

if __name__ == '__main__':
    app.run(port = 8000)