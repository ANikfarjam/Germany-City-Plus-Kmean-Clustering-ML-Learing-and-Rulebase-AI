#Author: Ashkan Nikfarjam
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc #a library and package to create nav bar and other components  
import plotly.express as px
import Analysis

with open("intro.txt",'r') as f:
    intro_text = f.read()
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/", active='exact')),
        dbc.NavItem(dbc.NavLink("Analysis", href="/Analysis", active='exact')),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("something", href="#"),
                dbc.DropdownMenuItem("something", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Germany ---",
    brand_href="#",
    color="dark",
    dark=True,
)

content = html.Div(id="page-content")
app.layout = html.Div([dcc.Location(id="url"), navbar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
         return html.Div([
        html.Div([
            html.P(intro_text, style={'width': '50%'}),  
            html.Div([
                html.Iframe(
                    src='https://docs.google.com/presentation/d/e/2PACX-1vTN00ZBzwqmcQe5cbG1XK4NeaUgCE-KtU2NgeB5VwlBoiO2nw5noUO1LewV_Ed01w/embed?start=false&loop=false&delayms=3000',
                    width='800px',
                    height='500px'
                ),
            ], style={'display': 'flex', 'alignItems': 'center'}),  # Centering the iframe horizontally
        ], style={'display': 'flex', 'flexDirection': 'row'}),
    ])

    elif pathname == "/Analysis":
        return html.Div([
            html.Div([
                html.Div(id='df_checkBox_container', children=[
                    dcc.Checklist(
                        id='df-checkbox',
                        options=[
                            {'label': 'Healthcare', 'value': 'healthcare'},
                            {'label': 'Rental', 'value': 'rental'},
                            {'label': 'Number of Schools', 'value': 'schoolCount'},
                            {'label': 'Population', 'value': 'population'}
                        ],
                        value=['healthcare']  # Default value(s)
                    ),
                ], style={'flex': '1'}),
                html.Div(id='graph-container', style={'flex': '3'}),
            ], style={'display': 'flex'}),
        ])
    elif pathname == "/assets/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

@app.callback(Output("graph-container", "children"), [Input("df-checkbox", "value")])
def update_graph(value):
    if "healthcare" in value:
        graph = dcc.Graph(figure=Analysis.scatterMap(Analysis.healthCare_df, 'Number of beds', 'Number of Hospitals'))
        return html.Div([html.Div(id='map', style={'width': '100%'}), graph])
    elif "rental" in value:
        graph = dcc.Graph(figure=Analysis.scatterMap(Analysis.rental_df, 'Price', 'Beds'))
        return html.Div([html.Div(id='map', style={'width': '100%'}), graph])
    elif "schoolCount" in value:
        graph = dcc.Graph(figure=Analysis.scatterMap(Analysis.school_df, size_column='Number of schools'))
        return html.Div([html.Div(id='map', style={'width': '100%'}), graph])
    elif "population" in value:
        graph = dcc.Graph(figure=Analysis.scatterMap(Analysis.mod_City, size_column='population'))
        return html.Div([html.Div(id='map', style={'width': '100%'}), graph])

if __name__=='__main__':
    app.run_server(debug=True)
