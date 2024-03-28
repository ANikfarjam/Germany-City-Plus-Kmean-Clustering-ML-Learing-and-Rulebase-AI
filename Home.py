#Author: Ashkan Nikfarjam
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc #a library and package to create nav bar and other components
import plotly.express as px
import Analysis

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
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
        return html.P(intro_text)
    elif pathname == "/Analysis":
        html.Div(id='map', style={'width': '100%'}),
        graph = dcc.Graph(figure=Analysis.fig)
        return graph
    elif pathname == "/page-2":
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


if __name__=='__main__':
    app.run_server(debug=True)
