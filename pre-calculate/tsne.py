import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.manifold import TSNE
import joblib

# Step 1: Load the MNIST dataset (70,000 samples, 28x28 pixel images)
mnist = fetch_openml('mnist_784', version=1)
raw = mnist.data  # This is the raw high-dimensional data (n_samples, n_features)
y = mnist.target

# Randomly sample a subset of the data for visualization purposes
sample_size = 5000  # Choose a smaller subset for easier computation
indices = np.random.choice(len(raw), sample_size, replace=False)
raw_sampled = raw.iloc[indices]
y_sample = y.iloc[indices]

# Step 2: Define perplexity values for different embeddings
perplexities = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# Dictionary to store raw data and embeddings for each perplexity
data_store = {}

# Step 3: Loop over perplexity values and calculate t-SNE embeddings
for perplexity in perplexities:
    
    print(f"perplexity: {perplexity}")
    
    tsne = TSNE(n_components=2, perplexity=perplexity, random_state=42)
    emb = tsne.fit_transform(raw_sampled)
    
    # Store both raw data and the corresponding embedding
    data_store[perplexity] = {'raw': raw_sampled, 'emb': emb, 'y': y_sample}
    
    # Save each embedding (both raw and embedded data)
    joblib.dump(data_store[perplexity], f'mnist_sample_{sample_size}_tsne_perplexity_{perplexity}.pkl')

print("Raw and embedded MNIST data stored and saved for all perplexities.")