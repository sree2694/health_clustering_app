import streamlit as st
import pandas as pd
from src.preprocessing import preprocess_data
from src.clustering import apply_kmeans, apply_dbscan, apply_hierarchical
from src.visualization import plot_clusters, plot_silhouette

st.set_page_config(page_title="Healthcare Clustering App", layout="wide")

st.title("🏥 Patient Health Clustering for Preventive Care")

uploaded_file = st.file_uploader("Upload Health CSV File", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📋 Raw Data Preview")
    st.dataframe(df.head())

    processed_df, scaled_data = preprocess_data(df)

    algo = st.selectbox("Select Clustering Algorithm", ["KMeans", "DBSCAN", "Hierarchical"])
    
    if algo == "KMeans":
        k = st.slider("Select number of clusters (K)", 2, 10, 3)
        labels, model = apply_kmeans(scaled_data, k)
        st.pyplot(plot_silhouette(scaled_data, labels))
    elif algo == "DBSCAN":
        eps = st.slider("Epsilon", 0.1, 5.0, 0.5)
        min_samples = st.slider("Min Samples", 2, 10, 5)
        labels, model = apply_dbscan(scaled_data, eps, min_samples)
    else:
        dist_metric = st.selectbox("Distance Metric", ["euclidean", "manhattan"])
        labels, model = apply_hierarchical(scaled_data, dist_metric)

    st.subheader("📊 Clustered Data")
    df["Cluster"] = labels
    st.dataframe(df)

    st.subheader("🧬 Cluster Visualization (PCA)")
    st.pyplot(plot_clusters(scaled_data, labels))
