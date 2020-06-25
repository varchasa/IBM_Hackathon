import pandas as pd
import plotly
import plotly.express as px

import dash             
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
file = pd.read_csv('responsesoflockdown.csv')
app.layout = html.Div([
  html.Div([
        dcc.Graph(id='our_graph')
    ],className='nine columns'),
    html.Div([

        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown',
            options = [
                      {'label' : 'Uttar Pradesh', 'value' : 'Uttar Pradesh' },
                      {'label' : 'Madhya Pradesh', 'value' : 'Madhya Pradesh' },
                      {'label' : 'Andhra Pradesh', 'value' : 'Andhra Pradesh' },
                      {'label' : 'Assam', 'value' : 'Assam' },
                      {'label' : 'Delhi', 'value' : 'Delhi' },
                      {'label' : 'Karnataka', 'value' : 'Karnataka' },
                      {'label' : 'West Bengal', 'value' : 'West Bengal' },
                      {'label' : 'Telangana', 'value' : 'Telangana' },
                      {'label' : 'Tamil Nadu', 'value' : 'Tamil Nadu' },
                      {'label' : 'Bihar', 'value' : 'Bihar' },
                      {'label' : 'Kerela', 'value' : 'Kerela' },
                      {'label' : 'Jharkhand', 'value' : 'Jharkhand' },
                      {'label' : 'Rajasthan', 'value' : 'Rajasthan' },
                      {'label' : 'Pondicherry', 'value' : 'Pondicherry' },
                      {'label' : 'Maharashtra', 'value' : 'Maharashtra' },
                      {'label' : 'Gujarat', 'value' : 'Gujarat' },
                      {'label' : 'Haryana', 'value' : 'Haryana' },
                      ],
                      optionHeight=35,
                      value = 'Uttar Pradesh',
                      searchable=True,
                      placeholder='Please select...',     
                      clearable=True,
                      style={'width':"100%"},
            ),                                  
                                              
    ],className='three columns'),
])

@app.callback(
    Output(component_id='our_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)             
def build_graph(column_chosen):
    df=file
    fig =px.pie(df,names=column_chosen)
    return fig

@app.callback(
    Output(component_id='output_data', component_property='children'),
    [Input(component_id='my_dropdown', component_property='search_value')]
)

def build_graph(data_chosen):
    return ('Search value was: " {} "'.format(data_chosen))

if __name__ == '__main__':
    app.run_server(debug=True)