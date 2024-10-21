from snc.snc import SNC
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
import joblib

import time

sample_size = 5000
# perplexities = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# TODO: change to full list, and change label none to y.asxxx
perplexities = [5]

# calc for each
for perplexity in perplexities:

	print(f'mnist_sample_{sample_size}_tsne_perplexity_{perplexity}.pkl')

	# Load stored data for a specific perplexity
	data = joblib.load(f'mnist_sample_{sample_size}_tsne_perplexity_{perplexity}.pkl')

	# Access raw and embedded data
	raw_data = data['raw']  # Original high-dimensional MNIST data
	emb_data = data['emb']  # t-SNE projection (2D)
	y = data['y']

	# print(y.iloc[0])

	# Visualize the embedded data (emb)
	# plt.scatter(emb_data[:, 0], emb_data[:, 1], c=y.astype(int), cmap='tab10')
	# plt.colorbar()
	# plt.title('t-SNE embedding (perplexity=5)')
	# plt.show()

	parameter = { "k": 'sqrt', "alpha": 0.1 }

	metrics = SNC(
	raw=raw_data, 
	emb=emb_data, 
	iteration=300, 
	dist_parameter = parameter
	)
	start_time = time.time()

	metrics.fit(record_vis_info=True) # enable visualization
	print(metrics.steadiness(), metrics.cohesiveness())
	metrics.vis_info(file_path=f'info_sample_{sample_size}_tsne_perplexity_{perplexity}.json', label=y.astype(int).tolist(), k=10)
	
	end_time = time.time()
	elapsed_time = end_time - start_time
	print(f"Time elapsed: {elapsed_time:.4f} seconds")
