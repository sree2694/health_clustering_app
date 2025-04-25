## 🏥 Healthcare Clustering App

An interactive **Streamlit** app that performs **Unsupervised Machine Learning (Clustering)** on healthcare data to discover patient groups with similar health profiles. Ideal for preventive care analysis, wellness programs, and health trend discovery.

---

### 📌 Features

- 📁 Upload your own health dataset (CSV)
- 🧪 Choose between **KMeans**, **DBSCAN**, or **Hierarchical Clustering**
- 📉 Visualize clusters using PCA (2D)
- 📊 View Silhouette Scores and cluster statistics
- ✅ Simple, browser-based UI using **Streamlit**

---

### 🧬 Example Use Cases

- Group patients with similar BMI, blood pressure, or activity levels
- Identify outlier health profiles with DBSCAN
- Assist in public health segmentation and profiling

---

### 📂 Folder Structure

```
health_clustering_app/
├── app.py
├── data/
│   └── sample_health_data.csv
├── src/
│   ├── preprocessing.py
│   ├── clustering.py
│   └── visualization.py
├── requirements.txt
└── README.md
```

---

### 🚀 How to Run

1. **Clone this repository**:
   ```bash
   git clone https://github.com/sree2694/health_clustering_app.git
   cd health_clustering_app
   ```

2. **Create a virtual environment** and activate:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

---

### 📈 Sample Input Columns

```csv
BMI,SleepTime,PhysicalHealth,MentalHealth,AlcoholConsumption,Smoking,Age
22.5,7,2,1,0,0,25
30.1,5,10,8,1,1,55
27.8,6,5,2,1,0,40
33.2,4,15,14,1,1,60
24.5,8,1,0,0,0,30
29.0,6,6,5,0,1,45
35.4,5,18,20,1,1,70
26.7,7,4,2,0,0,35
31.1,6,12,10,1,1,50
23.3,8,2,1,0,0,28
```

Make sure your dataset has **numerical health indicators**. Categorical features should be encoded or removed.

---

### 📜 License

This project is open-source under the [Apache License](LICENSE).

---