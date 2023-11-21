from dash import Dash, html, dcc
import plotly.express as px

#Creación de la app de dash

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        figure = px.scatter(x = ['Ingresos', 'Gastos', 'Ahorros'], y = [10000,4000,6000], labels = {'x': 'Eje X', 'y': 'Eje Y'}),
        id = 'scatter-plot'
    ) 
])

if __name__ == '__main__':
    app.run_server(port = 8000)