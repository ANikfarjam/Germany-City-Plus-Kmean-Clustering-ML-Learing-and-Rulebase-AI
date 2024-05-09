from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd


# def read_paragraphs(file_path):
#     with open(file_path, 'r') as file:
#         paragraphs = [[]]  # Initialize list to hold paragraphs
#         for line in file:
#             line = line.strip()  # Remove leading/trailing whitespaces
#             if line:  # If line is not empty
#                 paragraphs[-1].append(line)  # Append line to current paragraph
#             else:  # If line is empty, start a new paragraph
#                 paragraphs.append([])
#         # Combine lines within each paragraph into a single string
#         paragraphs = [' '.join(paragraph) for paragraph in paragraphs if paragraph]
#     return paragraphs
# paragraph = read_paragraphs('./assets/AIML.txt')
# with open('./Training/graphicKmean.py', 'r') as file:
#         instructions_kg = file.read()
with open('./assets/AIML.txt','r') as file:
    paragraph = file.readlines()
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
    html.P(paragraph[4]),
    html.Img(src='./assets/sqc.png', style={'align': 'center'}),  
    
    
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