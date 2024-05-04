# Author: Ryan Fernald

import json
import pandas as pd
import plotly.express as px

from Analysis import religion_df


# plotly library
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go

def find_state_name(geojson_file, state_name):

    with open(geojson_file, "r", encoding="utf-8") as f:
        geojson_data = json.load(f)

    for feature in geojson_data["features"]:
        if feature["properties"]["NAME_1"] == state_name:
            return feature["properties"]["NAME_1"]
        elif "VARNAME_1" in feature["properties"] and feature["properties"]["VARNAME_1"] == state_name:
            return feature["properties"]["NAME_1"]
    return None


def create_choropleth_map(df, geojson_file, location_column, value_column, title=None):
    """
    Create a choropleth map using Plotly.

    Args:
    - df: DataFrame containing the data.
    - geojson_file: Path to the GeoJSON file for the map.
    - location_column: Name of the column in df containing the location names. ALWAYS NAME THE IT STATE!!!
    - value_column: Name of the column in df containing the values to be mapped.
    - title: Title of the map (optional).

    Returns:
    - fig: Plotly figure object for the choropleth map.
    """

    # Map state names in df to names in GeoJSON file
    df['State'] = df[location_column].apply(lambda x: find_state_name(geojson_file, x))

    # Load GeoJSON file
    with open(geojson_file, "r", encoding="utf-8") as f:
        geojson_data = json.load(f)

    # Create choropleth map
    fig = px.choropleth(
        df,
        geojson=geojson_data,
        locations="State",
        color=value_column,
        featureidkey="properties.NAME_1",
        projection="mercator",
        title=title,
    )

    fig.update_geos(
        showcountries=True,
        showcoastlines=True,
        showland=True,
        fitbounds="locations",
        visible=False  
    )

    fig.update_layout(margin={"r": 30, "t": 30, "l": 30, "b": 30}) #margin adjustments are in pixels
    
    return fig
