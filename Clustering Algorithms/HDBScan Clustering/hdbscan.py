# Brandon Gurley
# 3-22-2022
# Senior Project
# HDBSCAN

import hdbscan
import pandas as pd
import numpy as np

from sklearn.datasets import load_digits
from sklearn.manifold import TSNE

import matplotlib.pyplot as plt
import seaborn as sns

netData = pd.read_csv("stressTest.csv")
timeSrc = pd.DataFrame(netData, columns= ['Time', 'Source Port'])
timeSrc = timeSrc.fillna(timeSrc.mean())
timeSrc= timeSrc.to_numpy()

clusterer = hdbscan.HDBSCAN(min_cluster_size=15).fit(timeSrc)
cluster_colors = [color_palette[x] if x >= 0
                  else (0.5, 0.5, 0.5)
                  for x in clusterer.labels_]
cluster_member_colors = [sns.desaturate(x, p) for x, p in
                         zip(cluster_colors, clusterer.probabilities_)]
plt.scatter(*projection.T, s=20, linewidth=0, c=cluster_member_colors, alpha=0.25)
labels = clusterer.labels_
plt.show()
