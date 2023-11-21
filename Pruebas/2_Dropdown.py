from dash import Dash, html, dcc

#Creación de la app de dash

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        options = [
            {'label': 'Ciencia de datos', 'value': 'CD'},
            {'label': 'Machine Learning', 'value': 'ML'},
            {'label': 'Despligue Web', 'value': 'DW'},
            {'label': 'Interfaces', 'value': 'I'}
        ], 
        
        value = 'CD'
    )
])

if __name__ == '__main__':
    app.run(port = 8000)