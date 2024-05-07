import pandas as pd

clustered_data = pd.read_csv('clustered_States.csv')
clustered_data = clustered_data.groupby(by='Region').mean().reset_index()
clustered_data['Cluster'] = clustered_data['Cluster'].astype(int)
print(clustered_data)
clustered_data.to_csv('clustered_recomend.csv',index=False)
