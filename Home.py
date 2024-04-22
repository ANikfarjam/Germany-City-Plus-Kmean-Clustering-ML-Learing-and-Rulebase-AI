#author: Ashkan Nikfarjam
import dash
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import Analysis
from assets import cards, scatterMap

with open("intro.txt", 'r') as f:
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
                html.Img(src="assets/walp.webp", style={'max-height': '50vh', 'width': '100%', 'object-fit': 'cover'}),
                html.P(intro_text, style={'padding': '32px 48px'}),
            ]),
            html.Div([
                html.Div(cards.history_card, style={'margin-right': '10px'}),
                html.Div(cards.questionare_card, style={'margin-left': '10px'}),
            ], style={'display': 'flex'}),
        ], style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center', 'align-items': 'center', 'height': '100vh'})

    elif pathname == "/Analysis":
        return html.Div([
            html.Div([
                html.Div(id='map selector', children=[
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dcc.RadioItems(
                                        id='df-checkbox1',
                                        options=[
                                            {'label': 'Hospitals', 'value': 'healthcare'},
                                            {'label': 'Pharmacy', 'value': 'num_pharmacy'}
                                        ],
                                        value='healthcare'  # Default value
                                    )
                                ],
                                title="Healthcare"
                            ),
                            dbc.AccordionItem(
                                [
                                    dcc.RadioItems(
                                        id='df-checkbox2',
                                        options=[
                                            {'label': 'Rental', 'value': 'rental'}
                                        ],
                                        #value='rental'
                                    )
                                ],
                                title="Rental"
                            ),
                            dbc.AccordionItem(
                                [
                                    dcc.RadioItems(
                                        id='df-checkbox3',
                                        options=[
                                            {'label': 'Number of Schools', 'value': 'schools'}
                                        ],
                                        #value='schools'
                                    )
                                ],
                                title="Education"
                            ),
                            dbc.AccordionItem(
                                [
                                    dcc.RadioItems(
                                        id='df-checkbox4',
                                        options=[
                                            {'label': 'Population', 'value': 'population'}
                                        ],
                                        #value='population'
                                    )
                                ],
                                title="Population"
                            )
                        ]
                    )
                ],style={'width': '250px'})
                , html.Div(id='graph-container',style={'width':'100%'})  # Add an empty div for the graph
            ],style={'display': 'flex'})
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

@app.callback([
   Output("df-checkbox1","value"), 
   Output("df-checkbox2","value"),
   Output("df-checkbox3","value"),
   Output("df-checkbox4","value")
   ], 
   [
   Input("df-checkbox1","value"), 
   Input("df-checkbox2","value"),
   Input("df-checkbox3","value"),
   Input("df-checkbox4","value")
   ]    
)
def sync_checkbox(value1, value2, value3, value4):
    print(value1,value2,value3,value4)
    ctx = dash.callback_context
    print(ctx.triggered)
    if not ctx.triggered:
        print('here')
        return value1, value2, value3, value4
    
    input_id = ctx.triggered[0]['prop_id']
    input_id = input_id.split(".")[0]

    if input_id == "df-checkbox1" and value1 is not None:
        return value1, None, None, None
    elif input_id == "df-checkbox2" and value2 is not None:
        return None, value2, None, None
    elif input_id == "df-checkbox3" and value3 is not None:
        return None, None, value3, None
    elif input_id == "df-checkbox4" and value4 is not None:
        return None, None, None, value4
    else:
        print("unexpected scenario:")
        print("input_id: " + input_id)
        print("values: " + (value1, value2, value3, value4))


@app.callback(Output("graph-container", "children"), [Input("df-checkbox1", "value"), Input("df-checkbox2", "value"), Input("df-checkbox3", "value"), Input("df-checkbox4", "value")])
def update_graph(value1, value2, value3, value4):
    print(value1, value2, value3, value4)
    # Prioritize the values based on the order of the radio buttons
    value = value4 or value3 or value2 or value1
    print(value)

    if value == "healthcare":
        graph = dcc.Graph(figure=scatterMap.plot_scatterMap(Analysis.healthCare_df, 'Number of beds', 'Number of Hospitals'))
        return html.Div([html.Div(id='map', style={'width': '100%'}), graph])    
    elif value == "rental":
        graph = dcc.Graph(figure=scatterMap.plot_scatterMap(Analysis.rental_df, 'Price', 'Beds'))
        return html.Div([html.Div(id='map', style={'width': '100%'}), graph])
    elif value == "schools":
        graph = dcc.Graph(figure=scatterMap.plot_scatterMap(Analysis.school_df, size_column='Number of schools'))
        return html.Div([html.Div(id='map', style={'width': '100%'}), graph])
    elif value == "population":
        graph = dcc.Graph(figure=scatterMap.plot_scatterMap(Analysis.mod_city, size_column='population'))
        return html.Div([html.Div(id='map', style={'width': '100%'}), graph])
    elif value == "num_pharmacy":
        graph = dcc.Graph(figure=scatterMap.plot_scatterMap(Analysis.pharmacy_df, size_column='number of pharmecies'))
        return html.Div([html.Div(id='map', style={'width': '100%'}), graph])
    


if __name__ == '__main__':
    app.run_server(debug=True)