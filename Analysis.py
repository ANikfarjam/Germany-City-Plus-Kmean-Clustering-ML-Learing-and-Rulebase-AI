#Author: Ashkan Nikfarjam
import plotly.express as px
import pandas as pd



HealthCare_data = pd.read_csv("./DATA/Helthcare/numberofHospitals.csv")
HealthCare_data.rename(columns={'City':'city'}, inplace=True)

city_df = pd.read_csv("./DATA/German cities.csv")
merged_df = pd.merge(city_df, HealthCare_data, on='city')


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

