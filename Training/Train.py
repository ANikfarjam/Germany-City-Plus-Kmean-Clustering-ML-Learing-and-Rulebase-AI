#author: Ashkan Nikfajram, Sean Hsieh, Ryan Fernald
#prepimg data for ML training
from itertools import groupby
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import sklearn.decomposition
import numpy as np
import plotly.graph_objects as go
import joblib

#the result of clustering gets graphed using this function
#inputed df has to be transformed into 3dimention
def calculate_inertia(data, centroids, labels):
    
    # Calculate inertia for the given data and centroids.
    
    # Args:
    # - data: The dataset for which to calculate inertia (numpy array).
    # - centroids: The coordinates for the cluster centers (numpy array).
    # - labels: The labels of the closest cluster center for each data point (numpy array).
    
    # Returns:
    # - inertia: The calculated inertia.
    
    inertia = 0
    for i, center in enumerate(centroids):
        cluster_data = data[labels == i]
        distances = np.linalg.norm(cluster_data - center, axis=1)
        inertia += np.sum(distances**2)
    return inertia
def plot_clustered(df):
    states_clustered_fig = go.Figure(data=[go.Scatter3d(
        x=df[0],  # PC1 values
        y=df[1],  # PC2 values
        z=df[2],  # PC3 values
        mode='markers',
        marker=dict(
            size=12,
            color=clustered_df['Cluster'],  # Color by cluster
            colorscale='Viridis',  # Choose colorscale
            opacity=0.8
        ),
        text=X_encoded.index,  # Display region name on each point
    )])

    # Update axis labels
    states_clustered_fig.update_layout(
        scene=dict(
            xaxis=dict(title='X Axis', tickvals=[], ticktext=[]),  # Hide x-axis numbers
            yaxis=dict(title='Y Axis', tickvals=[], ticktext=[]),  # Hide y-axis numbers
            zaxis=dict(title='Z Axis', tickvals=[], ticktext=[]),  # Hide z-axis numbers
        )
    )

    return states_clustered_fig

#importing german cities all the DFs gets merged based on the keys of this DF
set2 = pd.read_csv('./Training/resampling_germany_ratings.csv')
#set2 = set2.groupby(by='Region').mean().reset_index()

#grpahical confirmation of K-value
#finde number of oprimal cluster
def find_optimal_clusters(data, max_clusters=10):
    """
    Finds the optimal number of clusters using the elbow method.
    
    Args:
    - data: The dataset for clustering.
    - max_clusters: Maximum number of clusters to consider.
    
    Returns:
    - optimal_n_clusters: The optimal number of clusters.
    """
    sse = []  # Sum of squared distances for each number of clusters
    for k in range(1, max_clusters + 10):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)  # SSE for each k
    
    # Calculate the first derivative of SSE to find the elbow point
    first_derivative = np.diff(sse)
    
    # Find the index of the elbow point
    elbow_index = np.argmin(first_derivative) + 1  # Add 1 to account for zero-based indexing
    
    optimal_n_clusters = elbow_index + 1  # Add 1 to account for the zero-based index
    
    return optimal_n_clusters
###################################################################################
#trainint
###################################################################################
#set up traning data sets
if __name__=="__main__":
    X = set2.copy()
    X_encoded = pd.get_dummies(X, columns=['Region'])
    #X_encoded =  X.set_index('Region')
    print(X_encoded.columns)
    optimal_cluster = find_optimal_clusters(X_encoded)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_encoded.drop(columns=['Region_Bavaria', 'Region_Berlin',
        'Region_Brandenburg', 'Region_Bremen', 'Region_Hamburg', 'Region_Hesse',
        'Region_Lower Saxony', 'Region_Mecklenburg-Vorpommern',
        'Region_North Rhine-Westphalia', 'Region_Rhineland-Palatinate',
        'Region_Saarland', 'Region_Saxony', 'Region_Saxony-Anhalt',
        'Region_Schleswig-Holstein', 'Region_Thuringia']))
    print(X_scaled.shape)
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X_scaled)
    cluster_labels = kmeans.labels_
    #####

    # Add cluster labels to the DataFrame
    clustered_df = X_encoded.copy()
    clustered_df['Cluster'] = cluster_labels
    print(clustered_df.columns)
    region_columns = ['Region_Bavaria', 'Region_Berlin',
        'Region_Brandenburg', 'Region_Bremen', 'Region_Hamburg', 'Region_Hesse',
        'Region_Lower Saxony', 'Region_Mecklenburg-Vorpommern',
        'Region_North Rhine-Westphalia', 'Region_Rhineland-Palatinate',
        'Region_Saarland', 'Region_Saxony', 'Region_Saxony-Anhalt',
        'Region_Schleswig-Holstein', 'Region_Thuringia']
    regions = []

    # # Iterate over each row
    for index, row in clustered_df.iterrows():
        # Iterate over each region column
        for region_col in region_columns:
            # If the region column has a True value, add it to the regions list
            if row[region_col]:
                regions.append(region_col.split('_')[-1])
                break  
    clustered_df['Region'] = regions
    print(clustered_df.columns)
    clustered_df.drop(columns= region_columns, inplace=True)
    print(clustered_df.head())
    #clustered_df = clustered_df[['Cluster','Region']]
    clustered_df.to_csv('clustered_States.csv', index=False)
    coppy_df = clustered_df.copy()

    # Drop the 'Code' column
    #coppy_df.drop(columns='Code', inplace=True)

    # Set 'Region' as the index
    coppy_df.set_index('Region', inplace=True)


    data = coppy_df.values

    #print(data)


    # Perform PCA
    pca = sklearn.decomposition.PCA(n_components=3)
    decomposed = pca.fit_transform(data)
    print(decomposed)
    graph_data = pd.DataFrame(decomposed)
    print(graph_data.head())
    #graph_data.rename(columns={'1'})
    #droping regional thing from X_encode
#X_encoded.drop(columns=region_columns, inplace=True)
print(X_encoded.shape)
# fig.show()
training_fig =plot_clustered(graph_data)
########save our model to file so we can call predict from other location
joblib.dump(kmeans, '../Recomendation/kmeans_model.pkl')
training_fig.show()