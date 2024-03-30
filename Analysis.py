#Author: Ashkan Nikfarjam
import plotly.express as px
import pandas as pd

city_df = pd.read_csv("./DATA/German cities.csv")
#creating Rentals df for map
rental = pd.read_csv("./DATA/Rentals/cityRentals.csv")
rental.Price = rental.Price.astype(int)
rental  = rental.groupby(by=['Name','Beds']).Price.mean().reset_index()
#print(rental)
rental_pd = pd.DataFrame(rental).reset_index()
# Merge DataFrames on the 'city' column
rental_df = pd.merge(rental, city_df.copy(), how='left', left_on='Name', right_on='city')

# Drop the redundant 'city' column
rental_df.drop(columns=['city'], inplace=True)
rental_df = rental_df.rename({'Price':'Average Price'})
#print(rental_df.head())
#creating healthcare data frame for the map
HealthCare_data = pd.read_csv("./DATA/Helthcare/numberofHospitals.csv")
HealthCare_data.rename(columns={'City':'city'}, inplace=True)
healthCare_df = pd.merge(city_df.copy(), HealthCare_data, on='city')

#schools
school = pd.read_csv("./DATA/Education/matchedCitySchools.csv")
school_df = pd.merge(school, city_df.copy(), on='city', how='left')
print(school_df.head())

# environment
environment = pd.read_csv("./DATA/Environment/temperature_by_state.csv")
weather = pd.read_csv("./DATA/Environment/weather.csv")

# public transportation 
public_transportation = pd.read_csv("./DATA/Public Transportation/transportation.csv")

# politics
politics = pd.read_csv("./DATA/Politics/politics.csv")



#use this df for city population
mod_city = city_df.copy()
mod_city = mod_city.dropna()
def scatterMap(df, color_column=None, size_column=None):
    fig = px.scatter_mapbox(df, 
                        lat='lat',
                        lon='lng',
                        size= size_column,
                        color= color_column,
                        mapbox_style="carto-positron",
                        center={"lat": df['lat'].mean(), "lon": df['lng'].mean()},
                        color_continuous_scale="YlOrRd",  # Yellow to Red color scale
                        height=1000
                        )
    return fig