# Author: Sean H. & Ryan F.
# Date: Mat 2, 2024

# general import
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# plotly library
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go

''' The purposes of these plots are to show the difference between Western & Eastern Germany for some of the selected attributes
    Since plots can not be rendered here, here's the link to give you the idea how the plots will look like
    https://colab.research.google.com/drive/1QsK_06pE803Tq-WskwcZXCNCAVJz-7e7?usp=sharing
'''

# here we go!

#############
# EDUCATION # 
#############
univ_url = "https://raw.githubusercontent.com/ANikfarjam/CS133Project/main/DATA/Education/unvercities.csv"
univ_df = pd.read_csv(univ_url)

western_germany_cities = [
    'Aachen', 'Bonn', 'Bochum', 'Bremen', 'Cologne', 'Dortmund', 'Düsseldorf', 'Essen', 'Frankfurt',
    'Gelsenkirchen', 'Hagen', 'Hamburg', 'Hanover', 'Herne', 'Karlsruhe', 'Krefeld', 'Mannheim',
    'Mönchengladbach', 'Munich', 'Mülheim', 'Nuremberg', 'Oberhausen', 'Stuttgart', 'Wiesbaden',
    'Wuppertal'
] 
eastern_germany_cities = [
    'Berlin', 'Potsdam', 'Cottbus', 'Frankfurt (Oder)', 'Halle', 'Leipzig', 'Dresden', 'Chemnitz',
    'Magdeburg', 'Rostock', 'Schwerin', 'Erfurt', 'Jena', 'Gera', 'Zwickau', 'Dessau'
] 

western_univ_df = univ_df[univ_df['city'].isin(western_germany_cities)]
eastern_univ_df = univ_df[univ_df['city'].isin(eastern_germany_cities)]

trace1 = go.Bar(
                x = western_univ_df.city,
                y = western_univ_df['Total students'],
                name = "western university",
                marker = dict(color = 'rgba(150, 100, 11, 0.7)',
                             line=dict(color='rgb(0,0,0)',width=1.5)),
                text = western_univ_df['University'])
trace2 = go.Bar(
                x = eastern_univ_df.city,
                y = eastern_univ_df['Total students'],
                name = "eastern university",
                marker = dict(color = 'rgba(100, 150, 11, 0.7)',
                             line=dict(color='rgb(0,0,0)',width=1.5)),
                text = eastern_univ_df['University'])
data = [trace1, trace2]
layout = go.Layout(title = 'Germany Transportation 2022',
                   margin=dict(r=200, l=110, b=150, t=60))

university_plot_west_vs_east = go.Figure(data = data, layout = layout) # university plot

################################################################################################################################

#######
# GDP #
#######

income_url = "https://raw.githubusercontent.com/ANikfarjam/CS133Project/main/DATA/Income/city_income.csv"
income_df = pd.read_csv(income_url)

income_df = income_df.sort_values(['GDP in Billions'], ascending=False)
income_df = income_df[0:20]

eastern_germany_cities = [
    'Berlin', 'Dresden', 'Leipzig', 'Halle', 'Chemnitz', 'Magdeburg', 'Rostock', 'Erfurt', 'Jena', 'Gera', 'Zwickau', 'Dessau'
]

western_germany_cities = [
    'Hamburg', 'Munich', 'Frankfurt am Main', 'Cologne', 'Hannover region', 'Stuttgart', 'Düsseldorf', 'Nürnberg', 'Bremen', 
    'Bonn', 'Essen', 'Dortmund', 'Mainz', 'Aachen region', 'Karlsruhe', 'Mannheim', 'Braunschweig'
]

eastern_income_df = income_df[income_df['City'].isin(eastern_germany_cities)]
western_income_df = income_df[income_df['City'].isin(western_germany_cities)]
trace1 = go.Bar(
    x=eastern_income_df['City'],
    y=eastern_income_df['GDP in Billions'],
    name='Eastern Germany',
    marker=dict(color='rgb(31, 119, 180)'),  
    text=eastern_income_df['GDP in Billions'],
    textposition='auto'
)
trace2 = go.Bar(
    x=western_income_df['City'],
    y=western_income_df['GDP in Billions'],
    name='Western Germany',
    marker=dict(color='rgb(255, 127, 14)'),  
    text=western_income_df['GDP in Billions'],
    textposition='auto'
)

layout = go.Layout(
    title='Top 20 Cities by GDP in Billions (Eastern vs. Western Germany)',
    xaxis=dict(title='City'),
    yaxis=dict(title='GDP in Billions'),
    barmode='group'
)

gdp_plot_west_vs_east = go.Figure(data=[trace2, trace1], layout=layout) # GDP plot

################################################################################################################################

##################
# TRANSPORTATION # 
##################

public_transportation_url = "https://raw.githubusercontent.com/ANikfarjam/CS133Project/main/DATA/Public%20Transportation/transportation.csv"
public_transportation = pd.read_csv(public_transportation_url)
import pandas as pd
import plotly.graph_objs as go

eastern_germany_states = ['Berlin', 'Brandenburg', 'Mecklenburg-Vorpommern', 'Saxony', 'Saxony-Anhalt', 'Thuringia']
western_germany_states = ['Baden-Württemberg', 'Bavaria', 'Bremen', 'Hamburg', 'Hesse', 'Lower Saxony', 
                          'North Rhine-Westphalia', 'Rhineland-Palatinate', 'Saarland', 'Schleswig-Holstein']

eastern_transportation_df = public_transportation[public_transportation['states'].isin(eastern_germany_states)]
western_transportation_df = public_transportation[public_transportation['states'].isin(western_germany_states)]

trace1 = go.Bar(
    x=eastern_transportation_df['states'],
    y=eastern_transportation_df['easy_access_to_public_transportation_2022 (%)'],
    name='Eastern Germany',
    marker=dict(color='rgb(255, 133, 27)'),  
    text=eastern_transportation_df['easy_access_to_public_transportation_2022 (%)'],
    textposition='auto'
)

trace2 = go.Bar(
    x=western_transportation_df['states'],
    y=western_transportation_df['easy_access_to_public_transportation_2022 (%)'],
    name='Western Germany',
    marker=dict(color='rgb(255, 65, 54)'),  
    text=western_transportation_df['easy_access_to_public_transportation_2022 (%)'],
    textposition='auto'
)

layout = go.Layout(
    title='Ease of Access to Public Transportation in Germany (2022)',
    xaxis=dict(title='State'),
    yaxis=dict(title='Percentage of Easy Access to Public Transportation'),
    barmode='group'
)

transportation_west_vs_east = go.Figure(data=[trace2, trace1], layout=layout) # transportation plot 

################################################################################################################################

############
# RELIGION #
############





################################################################################################################################

#######################
# GEMANY east vs west #
#######################

germany_rating_url = "https://raw.githubusercontent.com/ANikfarjam/CS133Project/main/DATA/Sean%20data%20-%20help/Cultural/germany_state_ratings_1-10_various_categories.csv"
global_rating_url = "https://raw.githubusercontent.com/ANikfarjam/CS133Project/main/DATA/Sean%20data%20-%20help/Cultural/various_countries_ratings_1-10_categories.csv"

gremany_rating_df = pd.read_csv(germany_rating_url)

gremany_rating_df = gremany_rating_df.drop(['Country', 'Code'], axis=1)
eastern_germany_states = ['Berlin', 'Brandenburg', 'Mecklenburg-Vorpommern', 'Saxony', 'Saxony-Anhalt', 'Thuringia']
western_germany_states = ['Baden-Württemberg', 'Bavaria', 'Bremen', 'Hamburg', 'Hesse', 'Lower Saxony', 
                          'North Rhine-Westphalia', 'Rhineland-Palatinate', 'Saarland', 'Schleswig-Holstein']
eastern_germany_df = gremany_rating_df[gremany_rating_df['Region'].isin(eastern_germany_states)]
western_germany_df = gremany_rating_df[gremany_rating_df['Region'].isin(western_germany_states)]

eastern_germany_df = eastern_germany_df.drop(['Region'], axis=1)
western_germany_df = western_germany_df.drop(['Region'], axis=1)

west_mean_values = western_germany_df.mean()
east_mean_values = eastern_germany_df.mean()

west_df = pd.DataFrame(west_mean_values, columns=['Mean'])
west_df = pd.DataFrame(west_mean_values, columns=['Mean'])

trace1 = go.Scatter(
    x=east_mean_values.index,
    y=east_mean_values.values,
    mode='lines+markers',
    name='Eastern Germany',
    line=dict(color='rgb(31, 119, 180)'), 
)

trace2 = go.Scatter(
    x=west_mean_values.index,
    y=west_mean_values.values,
    mode='lines+markers',
    name='Western Germany',
    line=dict(color='rgb(255, 127, 14)'),
)

layout = go.Layout(
    title='Mean Ratings Comparison between Eastern and Western Germany',
    xaxis=dict(title='Categories'),
    yaxis=dict(title='Mean Rating'),
)

# Create figure
germany_rating_west_vs_east = go.Figure(data=[trace2, trace1], layout=layout) # west vs east rating

################################################################################################################################