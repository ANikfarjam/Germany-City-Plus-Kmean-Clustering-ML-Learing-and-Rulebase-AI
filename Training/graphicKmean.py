#author: Ashkan Nikfarjam
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.decomposition
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load data
data = pd.read_csv('resampling_germany_ratings.csv')

# Encode categorical variables
X_encoded = pd.get_dummies(data, columns=['Region'])

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Initialize PCA
pca = sklearn.decomposition.PCA(n_components=2)

# Initialize list to store cluster labels for each k
cluster_labels_list = []

# Iterate over different values of k
for k in range(1, 11):
    # Initialize KMeans with current k
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    cluster_labels = kmeans.labels_
    cluster_labels_list.append(cluster_labels)

# Plotting
num_rows = 2
num_cols = 5

fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 8))

for i, cluster_labels in enumerate(cluster_labels_list):
    row = i // num_cols
    col = i % num_cols
    ax = axes[row, col]

    pca.fit(X_scaled)
    decomposed = pca.transform(X_scaled)
    df = pd.DataFrame(decomposed, columns=['PCA1', 'PCA2'])
    df['Cluster'] = cluster_labels

    sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster', ax=ax, palette='viridis', legend=False)
    ax.set_title(f'k = {i+1}')
    ax.set_xlabel('PCA Component 1')
    ax.set_ylabel('PCA Component 2')

plt.tight_layout()
plt.savefig('../assets/cluster_plot.png')
#plt.show()