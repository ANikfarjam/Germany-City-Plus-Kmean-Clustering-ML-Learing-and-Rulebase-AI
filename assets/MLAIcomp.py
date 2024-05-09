#author: Ashkan NNikfarjam
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
#from Training import Train


with open('./assets/AIMLS.txt','r') as file:
    paragraph = file.readlines()
with open('./assets/ourmodel.txt') as file:
    mlP = file.readlines()
print(paragraph[3])
#set one
ma_page = html.Div([
    html.H1('Machine Learning and AI'),
    html.H2('Intro:'),
    html.P(paragraph[0]),  # Intro
    html.Video(
        src="./assets/KMeansClusteringAnimation.mp4",
        autoPlay=True,
        loop=True,
        controls=True,
        style={'width': '100%', 'height': 'auto'}  # Adjust width to 50% and height to auto
    ),
    html.P(paragraph[1]),
    html.H2('Calculating value of K:'),
    html.P(paragraph[2]),
    html.Div([
        html.Img(src='./assets/cluster_plot.png',style={'align': 'center'})
]),
    html.P(paragraph[3]), 
          
    html.Video(
        src="./assets/ElbowPlot.mp4",
        autoPlay=True,
        loop=True,
        controls=True,
        style={'width': '100%'}
    ),
    html.H2('Inertia'),
    html.P(paragraph[4]),
    html.P(paragraph[5]),
    html.Img(src='./assets/sqc.png', style={'align': 'center'}),  
    ###the google colab"
    html.H1('Our jurney:'),
    html.P(mlP[0]),
    html.P(mlP[1]),
    html.P(mlP[2]),
    html.P(mlP[3]),
    html.Img(src='./assets/KMvsHC.png', style={'align': 'center'}),
    html.Img(src='./assets/KMvsHR200.png', style={'align': 'center'}), 
    html.Img(src='./assets/KMvsHC4000.png', style={'align': 'center'}),   
    html.P(mlP[4]),
    html.H1('Artificial Inteligence'),
    html.P(paragraph[6]),
    html.Img(src='./assets/ai3-1.png', style={'align': 'center'}),
    html.P(paragraph[7]),
    #dcc.Graph(figure=Train.training_fig),  
    html.H2('Semantic Network'),
    html.P(paragraph[8]),
    html.Video(
        src="./assets/SemanticNetworkAnimation.mp4",
        autoPlay=True,
        loop=True,
        controls=True,
        style={'width': '100%'}
    ), 
    html.H2('Learning and RuleBased Agent'),
    html.P(paragraph[9]),
    html.P(paragraph[10]),
],style={'padding':'300px'})

##codeblock for code block
# @app.callback(
#     Output('output-graph', 'figure'),
#     [Input('interval-component', 'n_intervals')],
#     [dash.dependencies.State('code-input', 'value')]
# )
# def execute_code(n_intervals, code):
#     try:
#         exec(code, globals())
#         return fig
#     except Exception as e:
#         print(e)
#         return {}