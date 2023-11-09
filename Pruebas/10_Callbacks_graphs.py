#Definición de librerías
from dash import Dash, html, dcc
import pandas as pd
from dash.dependencies import Input, Output #Módulos de interactividad Input, Output
import plotly.graph_objs as go


#Carga de datos
df_temp = pd.read_excel(r'D:\Rigo\Rigo\Documentacion Tec Monterrey\Semestre Agosto-Diciembre\Analítica de datos y herramientas de IA II\Dash\Temperaturas.xlsx')

app = Dash(__name__)

#Definición del layout de la app a partir de componentes HTML y Core
app.layout = html.Div([
    dcc.Graph(id='graph_linea'),
    dcc.DatePickerRange(id='selector_fecha',start_date=df_temp['FECHA'].min(),end_date=df_temp['FECHA'].max()) #Seleccionamos todo el rango de fechas de nuestro dataframe
])

# CREACIÓN DE GRÁFICOS E INTERACTIVIDAD
#Callback para actualizar gráfico en función del rango de fechas seleccionadas
@app.callback(Output('graph_linea', 'figure'),
              [Input('selector_fecha', 'start_date'),Input('selector_fecha', 'end_date')])

def actualizar_graph(fecha_min, fecha_max):
    filtered_df = df_temp[(df_temp["FECHA"]>=fecha_min) & (df_temp["FECHA"]<=fecha_max)]
    #Creación de 1 traza por cada ciudad de nuestro dataframe
    traces = []
    for nombre_ciudad in filtered_df["Ciudad"].unique():
        df_ciudad = filtered_df[filtered_df['Ciudad'] == nombre_ciudad]
        traces.append(go.Scatter(
            x=df_ciudad["FECHA"],
            y=df_ciudad["T_Promedio"],
            text=df_ciudad["Ciudad"],
            mode='lines',
            opacity=0.7,
            marker={'size': 15},
            name=nombre_ciudad
        ))

    return { #Se retornan los objetos data y layout para ser enviados al Output con identificador graph_linea
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': 'Fecha'},
            yaxis={'title': 'Temperatura media'},
            hovermode='closest'
        )
    }

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server(port=8000)
