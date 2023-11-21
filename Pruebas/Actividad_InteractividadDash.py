#Importación de librerías necesarias
from dash import Dash, html, dcc
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

#Creación de la app de dash
app = Dash(__name__)

# Lectura del archivo csv tomando en cuanta su ubicación dentro del ordenador en cuestión
df_data = pd.read_csv(r'D:\Tecnologico de Monterrey\Clases\Semestre 7\Analitica II\UF5\Pruebas\SP500_data_.csv',
                      encoding = 'ISO-8859-1',delimiter=',')

#Se crea una variable con las opciones que se quieren para el dropdown
opciones = ['Open','Close']

#Creación del layout de Dash
app.layout = html.Div([
    #Creación del dropdown
        dcc.Dropdown(
            id='elec',
            options=[{'label': i, 'value': i} for i in opciones],
            value='Close'),
    #Creación del selector de fechas
        dcc.DatePickerRange(id='selector_fecha',
                            start_date=df_data['Date'].min(),
                            end_date=df_data['Date'].max()),
    #Creación de la gráfica que se vinculará al dropdown
        dcc.Graph(id='Abierto/Cerrado'),
    #Creación de la grafica de barras
        dcc.Graph(id='Bar')])

### CREACIÓN BASE DE LOS GRÁFICOS Y LA INTERACTIVIDAD ###
#Creación de callback para actualizar los gráficos en función del dropdown y el selector de fechas
@app.callback(
    [Output('Abierto/Cerrado', 'figure'),Output('Bar','figure')],
    [Input('elec', 'value'), Input('selector_fecha','start_date'), Input('selector_fecha','end_date')])

#Creación de función para la actualización de los datos
def actualizar_graficos(opcion,fecha_inicio,fecha_final):

    #Creación de los filtros en cuanto al selector de fechas
    filtro_fecha = df_data[(df_data['Date'] >= fecha_inicio) & (df_data['Date'] <= fecha_final)]

    #Creación base de la gráfica con el id 'selector fecha'
    elejido = {
        'data': [{'x': filtro_fecha['Date'], 
             'y': filtro_fecha[opcion], 
             'type': 'line', 
             'name': opcion}],

        'layout': go.Layout(title=f"Gráfico Histórico de Línea de {opcion}",
                    xaxis=dict(title="Años"),
                    yaxis=dict(title=f"{opcion}"))}
    
    #Creación base de la gráfica con el id 'Bar'
    volumen = {
        'data': [{'x': filtro_fecha['Date'], 
             'y': filtro_fecha['Volume'], 
             'type': 'bar', 
             'name': 'Volumen'}],

        'layout': go.Layout(title=f"Gráfico Histórico de Barras del Volumen",
                    xaxis=dict(title="Años"),
                    yaxis=dict(title="Volumen"))}
    
    #Se retornan las gréficas para integrarlas al layout
    return elejido, volumen

#Se ejecuta el programa Dash
if __name__ == '__main__':
    app.run(port = 8000)