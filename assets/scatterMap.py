import pandas as pd
from Analysis import city_df
import plotly.express as px
# general import
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Run this if plotly is not installed yet
#!pip install plotly==5.10.0


# plotly library
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
import plotly.graph_objs as go


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
                        color_continuous_scale="Portland",  # Yellow to Red color scale
                        height=1000
                        )
    return fig

