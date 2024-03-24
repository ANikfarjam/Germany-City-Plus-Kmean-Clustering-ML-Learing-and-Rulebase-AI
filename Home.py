#Author: Ashkan Nikfarjam
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc #a library and package to create nav bar and other components
import plotly.express as px


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="Home")),
        dbc.NavItem(dbc.NavLink("Analysis", href="Analysis")),
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


app.layout = html.Div([
    navbar,  # Include the navbar here
])

if __name__=='__main__':
    app.run_server(debug=True)
