import pandas as pd
from Analysis import city_df
import plotly.express as px
def plot_scatterMap(df, color_column=None, size_column=None):
    global city_df
    fig = px.scatter_mapbox(df, 
                        lat='lat',
                        lon='lng',
                        size= size_column,
                        color= color_column,
                        mapbox_style="carto-positron",
                        center={"lat": city_df['lat'].mean(), "lon": city_df['lng'].mean()},
                        zoom=5,
                        color_continuous_scale="YlOrRd",  # Yellow to Red color scale
                        height=1000
                        )
    return fig