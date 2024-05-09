import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram

# Load the data
data = pd.read_csv('resampling_4000.csv')
print(data.head())

# Drping State column
X = data.drop(columns='State')

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(X)

# Hierarchical Clustering
hierarchical = AgglomerativeClustering(n_clusters=3)
hierarchical_labels = hierarchical.fit_predict(X)

# Principal Component Analysis for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plotting the PCA-reduced data
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans_labels)
plt.title('PCA with K-Means Clustering')

plt.subplot(1, 2, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=hierarchical_labels)
plt.title('PCA with Hierarchical Clustering')

plt.show()

# For hierarchical clustering, also plotting the dendrogram
# Note: This might be computationally intensive for large datasets
plt.figure(figsize=(10, 7))
linkage_matrix = hierarchical.children_
dendrogram(linkage_matrix)
plt.title('Hierarchical Clustering Dendrogram')
plt.show()