
import pandas as pd
import plotly_express as px
import dash
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import Analysis
from assets import cards, scatterMap, chloroplethMap
import Visualization


with open("intro.txt", 'r') as f:
    intro_text = f.read()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/", active='exact')),
        dbc.NavItem(dbc.NavLink("Geo Analysis", href="/Analysis", active='exact')),
        dbc.NavItem(dbc.NavLink("State Analysis", href="/Visualization", active='exact')),
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
    brand="Germany City+",
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
                                            {'label': ' Hospitals', 'value': 'healthcare'},
                                            {'label': ' Pharmacy', 'value': 'num_pharmacy'}
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
                                            {'label': ' Rental', 'value': 'rental'}
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
                                            {'label': ' Number of Schools', 'value': 'schools'}
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
                                            {'label': ' Population', 'value': 'population'}
                                        ],
                                        #value='population'
                                    )
                                ],
                                title="Population"
                            ),
                            dbc.AccordionItem(
                                [
                                dcc.RadioItems(
                                    id='religion-selector',
                                        options=[
                                            {'label': ' Protestant', 'value': 'Protestant'},
                                            {'label': ' Catholic', 'value': 'Catholic'},
                                            {'label': ' Non-religious', 'value': 'Nonrel'},
                                            {'label': ' Muslim', 'value': 'Muslim'},
                                            {'label': ' Other Religion', 'value': 'Other'}
                                        ],
                                        #value='Protestant'
                                    )
                                ],
                                title = "Religion"
                            ),
                            dbc.AccordionItem(
                                [
                                    dcc.RadioItems(
                                        id='df-checkbox5',
                                        options=[
                                            {'label': 'Population with at least secondary education', 'value': 'Population with at least secondary education'},
                                            {'label': 'Employment rate', 'value': 'Employment rate'},
                                            {'label': 'Unemployment rate', 'value': 'Unemployment rate'},
                                            {'label': 'Household disposable income per capita', 'value': 'Household disposable income per capita'},
                                            {'label': 'Homicide rate', 'value': 'Homicide rate'},
                                            {'label': 'Mortality rate', 'value': 'Mortality rate'},
                                            {'label': 'Life expectancy', 'value': 'Life expectancy'},
                                            {'label': 'Air pollution (level of PM2.5)', 'value': 'Air pollution (level of PM2.5)'},
                                            {'label': 'Voter turnout', 'value': 'Voter turnout'},
                                            {'label': 'Broadband access', 'value': 'Broadband access'},
                                            {'label': 'Internet download speed 2021-Q4', 'value': 'Internet download speed 2021-Q4'},
                                            {'label': 'Number of rooms per person', 'value': 'Number of rooms per person'},
                                            {'label': 'Perceived social network support', 'value': 'Perceived social network support'},
                                            {'label': 'Self assessment of life satisfaction', 'value': 'Self assessment of life satisfaction'}
                                        ],
                                        #value='Population with at least secondary education'  # Default value
                                    )
                                ],
                                title="Social Indicators",
                            ),
                            dbc.AccordionItem(
                                [
                                    dcc.RadioItems(
                                        id='df-checkbox6',
                                        options=[
                                            {'label': 'Education', 'value': 'Education'},
                                            {'label': 'Jobs', 'value': 'Jobs'},
                                            {'label': 'Income', 'value': 'Income'},
                                            {'label': 'Safety', 'value': 'Safety'},
                                            {'label': 'Health', 'value': 'Health'},
                                            {'label': 'Environment', 'value': 'Environment'},
                                            {'label': 'Civic engagement', 'value': 'Civic engagement'},
                                            {'label': 'Accessibility to services', 'value': 'Accessibility to services'},
                                            {'label': 'Housing', 'value': 'Housing'},
                                            {'label': 'Community', 'value': 'Community'},
                                            {'label': 'Life satisfaction', 'value': 'Life satisfaction'}
                                        ],
                                        # value='Education'  # Default value
                                    )
                                ],
                                title="State Ratings #/10"
                            ),
                            dbc.AccordionItem(
                                [
                                    dcc.RadioItems(
                                        id='df-checkbox7',
                                        options=[
                                            {'label': 'Social Democratic Party of Germany', 'value': 'Social Democratic Party of Germany'},
                                            {'label': 'Union Parties (CDU/CSU)', 'value': 'Union Parties (CDU/CSU)'},
                                            {'label': 'Alliance 90/The Greens', 'value': 'Alliance 90/The Greens'},
                                            {'label': 'Free Democratic Party', 'value': 'Free Democratic Party'},
                                            {'label': 'Alternative for Germany', 'value': 'Alternative for Germany'},
                                            {'label': 'The Left', 'value': 'The Left'},
                                            {'label': 'Others', 'value': 'Others'}
                                        ],
                                        # value='Social Democratic Party of Germany'  # Default value
                                    )
                                ],
                                title="Political Parties"
                            )
                        ]
                    )
                ],style={'width': '250px'})
                , html.Div(id='graph-container', style={'width': '100%', 'height': '90vh', 'overflow-y': 'auto'})  # Add an empty div for the graph
            ], style={'display': 'flex'})
        ])
    
    elif pathname == "/assets/page-2":
        return html.P("Oh cool, this is page 2!")
    
    elif pathname == "/Visualization":
        return html.Div([
            dcc.Graph(figure=Visualization.university_plot_west_vs_east),
            dcc.Graph(figure=Visualization.gdp_plot_west_vs_east),
            dcc.Graph(figure=Visualization.transportation_west_vs_east),
            dcc.Graph(figure=Visualization.germany_rating_west_vs_east),
        ])


    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

@app.callback(
    [
        Output("df-checkbox1", "value"), 
        Output("df-checkbox2", "value"),
        Output("df-checkbox3", "value"),
        Output("df-checkbox4", "value"),
        Output("religion-selector", "value"),
        Output("df-checkbox5", "value"),
        Output("df-checkbox6", "value"),
        Output("df-checkbox7", "value")  
    ], 
    [
        Input("df-checkbox1", "value"), 
        Input("df-checkbox2", "value"),
        Input("df-checkbox3", "value"),
        Input("df-checkbox4", "value"),
        Input("religion-selector", "value"),
        Input("df-checkbox5", "value"),
        Input("df-checkbox6", "value"),
        Input("df-checkbox7", "value")  
    ]    
)

def sync_checkbox(value1, value2, value3, value4, religion_value, social_indicator_value, state_ratings, politics_value):
    print(value1, value2, value3, value4, religion_value, social_indicator_value, state_ratings, politics_value)
    ctx = dash.callback_context
    print(ctx.triggered)
    if not ctx.triggered:
        print('here')
        return value1, value2, value3, value4, religion_value, social_indicator_value, state_ratings, politics_value
    
    input_id = ctx.triggered[0]['prop_id']
    input_id = input_id.split(".")[0]

    if input_id == "df-checkbox1" and value1 is not None:
        return value1, None, None, None, None, None, None, None
    elif input_id == "df-checkbox2" and value2 is not None:
        return None, value2, None, None, None, None, None, None
    elif input_id == "df-checkbox3" and value3 is not None:
        return None, None, value3, None, None, None, None, None
    elif input_id == "df-checkbox4" and value4 is not None:
        return None, None, None, value4, None, None, None, None
    elif input_id == "religion-selector" and religion_value is not None:
        return None, None, None, None, religion_value, None, None, None
    elif input_id == "df-checkbox5" and social_indicator_value is not None:
        return None, None, None, None, None, social_indicator_value, None, None
    elif input_id == "df-checkbox6" and state_ratings is not None:  
        return None, None, None, None, None, None, state_ratings, None
    elif input_id == "df-checkbox7" and politics_value is not None:  
        return None, None, None, None, None, None, None, politics_value
    else:
        print("unexpected scenario:")
        print("input_id: " + input_id)
        print("values: " + (value1, value2, value3, value4, religion_value, social_indicator_value, state_ratings, politics_value))



@app.callback(Output("graph-container", "children"),
               [Input("df-checkbox1", "value"),
                Input("df-checkbox2", "value"),
                Input("df-checkbox3", "value"),
                Input("df-checkbox4", "value"),
                Input("religion-selector", "value"),
                Input("df-checkbox5", "value"),
                Input("df-checkbox6", "value"),
                Input("df-checkbox7", "value")]) 
def update_graph(value1, value2, value3, value4, religion_value, social_indicator_value, state_ratings, political_value):
    print(value1, value2, value3, value4, religion_value, social_indicator_value, state_ratings, political_value)  # For debugging
    # Prioritize the values based on the order of the radio buttons
    value = value4 or value3 or value2 or value1 or religion_value or social_indicator_value or state_ratings or political_value
    print(value)

    if value == "healthcare":
        graph = dcc.Graph(figure=scatterMap.plot_scatterMap(Analysis.healthCare_df, 'Number of beds', 'Number of Hospitals'))
    elif value == "rental":
        graph = dcc.Graph(figure=scatterMap.plot_scatterMap(Analysis.rental_df, 'Price', 'Beds'))
    elif value == "schools":
        graph = dcc.Graph(figure=scatterMap.plot_scatterMap(Analysis.school_df, size_column='Number of schools'))
    elif value == "population":
        graph = dcc.Graph(figure=scatterMap.plot_scatterMap(Analysis.mod_city, size_column='population'))
    elif value == "num_pharmacy":
        graph = dcc.Graph(figure=scatterMap.plot_scatterMap(Analysis.pharmacy_df, size_column='number of pharmecies'))
    elif value in ["Protestant", "Catholic", "Nonrel", "Muslim", "Other"]:
        fig = chloroplethMap.create_choropleth_map(Analysis.religion_df, "assets/germany-states.geojson", "State", religion_value)
        graph = dcc.Graph(figure=fig)
    elif value in ["Population with at least secondary education", "Employment rate", "Unemployment rate", "Household disposable income per capita", 
                   "Homicide rate", "Mortality rate", "Life expectancy", "Air pollution (level of PM2.5)", "Voter turnout", "Broadband access",
                   "Internet download speed 2021-Q4", "Number of rooms per person", "Perceived social network support", "Self assessment of life satisfaction"]:
        fig = chloroplethMap.create_choropleth_map(Analysis.indicators_df, "assets/germany-states.geojson", "State", value)
        graph = dcc.Graph(figure=fig)
    elif value in ["Education", "Jobs", "Income", "Safety", "Health", "Environment", "Civic engagement", "Accessibility to services", 
                   "Housing", "Community", "Life satisfaction"]: #BE CAREFUL OF TABBING HERE IT NEEDS TO BE PERFECT
        fig = chloroplethMap.create_choropleth_map(Analysis.stateratings_df, "assets/germany-states.geojson", "State", value)
        graph = dcc.Graph(figure=fig)
    elif value in ["Social Democratic Party of Germany", "Union Parties (CDU/CSU)", "Alliance 90/The Greens",
                    "Free Democratic Party", "Alternative for Germany", "The Left", "Others"]: 
        fig = chloroplethMap.create_choropleth_map(Analysis.politics_df, "assets/germany-states.geojson", "State", value)
        graph = dcc.Graph(figure=fig)

    else:
        # Return an empty div if no valid value is selected
        graph = html.Div()

    return html.Div([html.Div(id='map', style={'width': '100%'}), graph])
    


if __name__ == '__main__':
    app.run_server(debug=True)
