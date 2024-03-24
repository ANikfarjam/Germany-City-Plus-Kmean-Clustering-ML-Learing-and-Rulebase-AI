#Author: Ashkan Nikfarjam
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc #a library and package to create nav bar and other components
import plotly.express as px
import pandas as pd
import json

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("About", href="Home.py")),
        dbc.NavItem(dbc.NavLink("Analysis", href="Analysis.py")),
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

HealthCare_data = pd.read_csv("./DATA/Helthcare/numberofHospitals.csv")
HealthCare_data.rename(columns={'City':'city'}, inplace=True)

city_df = pd.read_csv("./DATA/German cities.csv")
merged_df = pd.merge(city_df, HealthCare_data, on='city')

# Read GeoJSON data
with open("./DATA/de.json", "r") as f:
    geojson_data = json.load(f)

# Create choropleth map figure
fig = px.scatter_mapbox(merged_df, 
                        lat='lat',
                        lon='lng',
                        size='Number of Hospitals',
                        color='Number of beds',
                        mapbox_style="carto-positron",
                        center={"lat": merged_df['lat'].mean(), "lon": merged_df['lng'].mean()},
                        color_continuous_scale="YlOrRd",  # Yellow to Red color scale
                        height=1000
                        )

app.layout = html.Div([
    navbar,  # Include the navbar here
    html.Div(id='map', style={'width': '100%'}),
    dcc.Graph(figure=fig)
])

if __name__=='__main__':
    app.run_server(debug=True)