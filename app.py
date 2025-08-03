from flask import Flask, render_template
import pandas as pd
from sklearn.decomposition import PCA
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('digits_sample_4cols.csv')
    X = df[['feature_1', 'feature_2', 'feature_3', 'feature_4']]
    y = df['label']

    pca = PCA(n_components=2)
    components = pca.fit_transform(X)
    df_pca = pd.DataFrame(components, columns=['PC1', 'PC2'])
    df_pca['Digit'] = y

    fig = px.scatter(df_pca, x='PC1', y='PC2', color='Digit',
                     title='2D PCA of Digits Dataset',
                     color_continuous_scale='Viridis',
                     labels={'Digit': 'Digit Label'})
    plot_html = fig.to_html(full_html=False)

    return render_template('index.html', plot_html=plot_html)
if __name__ == '__main__':
    print("Visit: http://localhost:5000")
    app.run(debug=True)
