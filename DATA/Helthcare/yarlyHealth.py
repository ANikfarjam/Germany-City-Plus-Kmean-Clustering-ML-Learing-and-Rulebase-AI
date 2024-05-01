#author: Ashkan Nikfarjam
#data source: https://www-genesis.destatis.de/genesis/online?operation=abruftabelleBearbeiten&levelindex=1&levelid=1712369404793&auswahloperation=abruftabelleAuspraegungAuswaehlen&auswahlverzeichnis=ordnungsstruktur&auswahlziel=werteabruf&code=23111-0001&auswahltext=&werteabruf=start#abreadcrumb
import pandas as pd
import plotly.express as px

data = pd.read_csv("hospitalsYR.csv", sep=';', skipfooter=3, engine='python')
print(data.columns)
data[' Number of Patients'] = data[' Number of Patients'].apply(lambda x: x*0.001)
data.rename(columns={' Number of Patients':'Number of Patients multiply by 100'},inplace=True)
plot_df = data[['year','Number of Hospitals', 'Number of Patients multiply by 100','Average length of stay']]

# Melt the DataFrame for easier plotting
melted_df = data.melt(id_vars=['year'], 
                    value_vars=['Number of Hospitals', ' Number of Beds', 'Number of Patients multiply by 100', 'Average length of stay', 'Average occupancy of hospital beds'], 
                    var_name='Stats', 
                    value_name='Values')
print(melted_df)
fig1= px.scatter(data, x='year', y='Number of Patients multiply by 100', size='Number of Hospitals', color='Average length of stay', 
                 title='Healthcare Stats Over Time',
                 size_max=50)
fig2 = px.bar(melted_df, x='Stats', y='Values',
              hover_name='Stats', 
              title='Healthcare Stats Over Time',
              animation_frame='year',
              labels={'Stats': 'Stats', 'Values': 'Values'},
              log_y=True)  # Set logarithmic scale for the y-axis so significantly small values are visible

# Show plot
fig1.show()