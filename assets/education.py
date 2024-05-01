import json
import plotly.graph_objects as go

with open("school.json", 'r') as file:
    geo_data = json.load(file)
locations = []
text = []
for feature in geo_data['features']:
    if 'geometry' in feature and 'coordinates' in feature['geometry']:
        coordinates = feature['geometry']['coordinates']
        locations.append(coordinates)
        city = feature['properties'].get('addr:city', '')
        name = feature['properties'].get('name', '')
        text.append(f"{name}, {city}")
educationMap = go.Scattermapbox(
    lat=[location[1] for location in locations],
    lon=[location[0] for location in locations],
    mode='markers',
    marker=dict(
        size=10,
        color='blue',
        opacity=0.7
    ),
    text=text,
)
# Define layout for the map
layout = go.Layout(
    title='School Locations',
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        style='open-street-map',
        zoom=10,
        center=dict(
            lat=sum([location[1] for location in locations]) / len(locations),
            lon=sum([location[0] for location in locations]) / len(locations)
        )
    ),
)

# Create the figure
fig = go.Figure(data=[educationMap], layout=layout)
fig.show()