import dash
from dash import dcc,html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

data = {
    'area': [100,200,300,400,500,600,700,800,900],
    'cost': [90,140,260,320,410,480,510,670,880]
}

df = pd.DataFrame(data)

app.layout = html.Div([html.H1('A Creation of Komal'),
html.H2('A Custom graph Visualization Tool'),
dcc.Dropdown(
    id = 'graph_type',
    options = [
        {'label':'Line Plot', 'value':'line'},
        {'label':'Bar Plot', 'value':'bar'},
        {'label':'Scatter Plot', 'value':'scatter'}


        
    ]
),
dcc.Graph(id = 'graph')],
style={'textAlign':'center','color':'purple','background':'#98F5F9'})

@app.callback(
    Output('graph','figure'),
    [Input('graph_type','value')]
    
)

def update_graph(graph_type):
    if graph_type == 'line':
        fig = px.line(df, x= 'area', y = 'cost')
    elif graph_type == 'bar':
        fig = px.bar(df, x= 'area', y = 'cost')
    else:
        fig= px.scatter(df, x = 'area', y = 'cost')

    return fig

app.run(debug= True)