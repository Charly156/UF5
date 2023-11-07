
from dash import Dash, html, dcc

#Creación de la app de dash

app = Dash(__name__)

app.layout = html.Div([
        html.Label('Inserta tu respuesta en el siguiente espacio: '),
        dcc.Input(id = 'my-input', value = 'Escribe algo', type = 'text')
])

if __name__ == '__main__':
    app.run(port = 8000)