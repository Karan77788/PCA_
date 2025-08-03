# PCA_

# PCA Visualization Web App (Flask)
```
This project is a simple Flask web app that performs **Principal Component Analysis (PCA)** on a small sample dataset (digit-like features) and visualizes the 2D PCA-reduced data using Plotly.
```

##  Project Overview
```
- **Algorithm**: Principal Component Analysis (PCA)
- **Use Case**: Dimensionality reduction of high-dimensional data (4D → 2D)
- **Tech Stack**:
  - Python (scikit-learn, pandas, numpy)
  - Flask (backend)
  - Plotly (interactive visualization)
- **Dataset**: 30 samples with 4 synthetic features
```


##  Project Structure
```
pca_flask_app/
├── app.py # Main Flask application
├── pca_data.csv # Sample data (4D input)
├── templates/
│ └── index.html # Frontend template with Plotly chart
├── static/
│ └── style.css # Optional styling
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

##  How to Run
### 1. Clone or download the repository

```
git clone https://github.com/yourusername/pca-flask-app.git
cd pca-flask-app
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the Flask app
```
python app.py
```
# Features
```
Performs PCA (2 components)

2D scatter plot with clusters labeled

Interactive zoom, hover, and tooltips with Plotly

Simple UI using HTML + CSS
```
#  Dependencies
```
Flask
pandas
numpy
scikit-learn
plotly
```
# Why PCA?
```
PCA helps reduce the dimensionality of datasets while preserving most of the variance. It's ideal for visualizing high-dimensional data such as images, sensor readings, or tabular data.
```
# ScreenShots

![alt text](<Screenshot 2025-08-03 170653.png>)
![alt text](<Screenshot 2025-08-03 170707.png>)
