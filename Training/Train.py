#author: Ashkan Nikfajram

from matplotlib.pyplot import xscale
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import sklearn.decomposition
import numpy as np
import plotly.graph_objects as go
import joblib

#the result of clustering gets graphed using this function
#inputed df has to be transformed into 3dimention
def plot_all_points(df, cluster_labels):
    pca = sklearn.decomposition.PCA(n_components=3)
    data = df.values
    decomposed = pca.fit_transform(data)

    fig = go.Figure()
    for cluster_label in np.unique(cluster_labels):
        cluster_indices = np.where(cluster_labels == cluster_label)[0]
        fig.add_trace(go.Scatter3d(
            x=decomposed[cluster_indices, 0],
            y=decomposed[cluster_indices, 1],
            z=decomposed[cluster_indices, 2],
            mode='markers',
            marker=dict(
                size=12,
                opacity=0.8,
                color=cluster_label,  # Use cluster label as color
                colorscale='Viridis'  # You can change the colorscale if needed
            ),
            name=f'Cluster {cluster_label}'
        ))

    fig.update_layout(
        scene=dict(
            xaxis=dict(title='X Axis', tickvals=[], ticktext=[]),
            yaxis=dict(title='Y Axis', tickvals=[], ticktext=[]),
            zaxis=dict(title='Z Axis', tickvals=[], ticktext=[]),
        )
    )

    return fig


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
    region_columns = ['Region_Bavaria', 'Region_Berlin',
        'Region_Brandenburg', 'Region_Bremen', 'Region_Hamburg', 'Region_Hesse',
        'Region_Lower Saxony', 'Region_Mecklenburg-Vorpommern',
        'Region_North Rhine-Westphalia', 'Region_Rhineland-Palatinate',
        'Region_Saarland', 'Region_Saxony', 'Region_Saxony-Anhalt',
        'Region_Schleswig-Holstein', 'Region_Thuringia']
    #normalize the features scales
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(set2.drop(columns='Region'))
    optimal_cluster = find_optimal_clusters(X_scaled)
    print("optimal cluster calculated at: ", optimal_cluster, "but we setting the modole to 3 due to lower inertia")
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X_scaled)
    #X_scaled['Cluster'] = kmeans.labels_ #this is an nparray

    
    coppy_df = pd.DataFrame(X_scaled)
    coppy_df.columns = set2.columns[1:]
    coppy_df['Cluster'] = kmeans.labels_ #this is an nparray
    coppy_df.to_csv('clustered_States.csv', index=False)
    print(coppy_df.head())

    
training_fig =plot_all_points(coppy_df, kmeans.labels_)
joblib.dump(kmeans, './Recomendation/kmeans_model.pkl')
training_fig.show()