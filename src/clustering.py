from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score

def apply_kmeans(data, k):
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(data)
    return labels, model

def apply_dbscan(data, eps, min_samples):
    model = DBSCAN(eps=eps, min_samples=min_samples)
    labels = model.fit_predict(data)
    return labels, model

def apply_hierarchical(data, metric):
    model = AgglomerativeClustering(distance_threshold=None, n_clusters=3, metric=metric, linkage='ward')
    labels = model.fit_predict(data)
    return labels, model
