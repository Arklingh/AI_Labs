import numpy as np
from sklearn import metrics
from sklearn.cluster import KMeans

def getQuality(data, rng = range(2,15)):
    scores = []
    values = rng

    for k in values:
        kmeans = KMeans(init='k-means++', n_clusters=k, n_init=10)
        kmeans.fit(data)
        score = metrics.silhouette_score(data, kmeans.labels_, metric='euclidean', sample_size=len(data))

        scores.append(score)

    num_clusters = np.argmax(scores) + values[0]

    return [scores, num_clusters]