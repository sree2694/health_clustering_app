import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, silhouette_samples

def plot_clusters(data, labels):
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(data)
    plt.figure(figsize=(8,6))
    plt.scatter(reduced[:,0], reduced[:,1], c=labels, cmap='tab10')
    plt.title("PCA - Cluster Visualization")
    return plt

def plot_silhouette(data, labels):
    score = silhouette_score(data, labels)
    plt.figure(figsize=(8,3))
    plt.title(f"Silhouette Score: {score:.2f}")
    return plt
