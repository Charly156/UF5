from dash import Dash, html

#Creación de la app de dash

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children = 'Hello World')
])

if __name__ == '__main__':
    app.run(debug = True)