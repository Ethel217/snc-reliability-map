# Visualization based on [Steadiness & Cohesiveness](https://github.com/hj-n/steadiness-cohesiveness#methods) and [reliability map](https://github.com/hj-n/snc-reliability-map)

Check original repo for detailed usage.

Educational implementation for IN4310 Seminar Computer Graphics (2024/25 Q1).

Sampled 5000 points from MNIST dataset, precaculate t-SNE with different perplexities (Same random space).

The dataset comes with labels, click on "show labels" to see labels color coded. Scroll to see different perplexity results.

Flowchart for better understanding of cluster distorsions and its relation with perplexity. Click on distorsion to see the corresponding t-SNE map.

## Files

per-calculate: tsne.py calculate t-SNE embeddings for 10 different perplexity values. scn.py calculate S&C visualization info for the embeddings.

## ChangeLog
use npm ver 16 LTS

## Citation
H. Jeon, H.-K. Ko, Y. Kim, J. Jo, and J. Seo, “Measuring and explaining the inter-cluster reliability of multidimensional projections,” IEEE Transactions on Visualization and Computer Graphics (TVCG, Proc. VIS), 2021.