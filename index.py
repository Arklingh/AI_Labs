import matplotlib.pyplot as plt
import numpy as np

import clstrs
import clustering_quality

data = np.loadtxt('lab01.csv', delimiter=';')

# show input data
plt.scatter(data[:,0], data[:,1], marker='x', color='black')

plt.title('Input data')
plt.show()

# train ms_model
clstr = clstrs
clstr.trainModel(data)

# get cluster centers
labels, cluster_centers, num_clusters = clstr.getClusters()

# show cluster centers
print('Number of clusters in input data = ', num_clusters)

markers = '*+sv.p^>'
plt.figure()

for i, marker in zip(range(num_clusters), markers):
    plt.scatter(data[labels==i, 0], data[labels==i, 1], marker=marker)

    cluster_center = cluster_centers[i]
    plt.plot(cluster_center[0], cluster_center[1], marker = 'o', markeredgecolor = 'black', markersize = 15)

plt.title('Clusters')
plt.show()

# get quality
values = range(2, 15)
scores, num_clusters = clustering_quality.Quality(data, values)

# show quality
for i, score in zip(values, scores):
    print('Number of clusters = ', i)
    print('Silhouette score = ', score)

print('Optimal cluster number: ', num_clusters)

plt.figure()
plt.bar(values, scores, width = 0.7, color = 'black', align = 'center')

plt.title('Cluster quality')
plt.show()

# get cluster areas
output, x_vals, y_vals = clstr.getClusterAreas(data)

# show cluster areas
plt.figure(1)
plt.clf()
plt.imshow(output, interpolation='nearest', extent=(x_vals.min(), x_vals.max(), y_vals.min(), y_vals.max()), cmap=plt.cm.Paired, aspect='auto', origin='lower')

for i, marker in zip(range(num_clusters), markers):
    plt.scatter(data[labels==i, 0], data[labels==i, 1], marker = marker)

    cluster_center = cluster_centers[i]
    plt.plot(cluster_center[0], cluster_center[1], marker = 'o', markeredgecolor = 'black', markersize = 15)

plt.title('Cluster areas (k = {})'.format(num_clusters))
plt.show()