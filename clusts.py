import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth

ms_model = None

def trainModel(data):
    bandwidth_data = estimate_bandwidth(data, quantile = 0.15, n_samples = len(data))

    global ms_model
    ms_model = MeanShift(bandwidth = bandwidth_data, bin_seeding = True)
    ms_model.fit(data)

def getClusters():
    cluster_centers = ms_model.cluster_centers_
    labels = ms_model.labels_
    num_clusters = len(np.unique(labels))

    return [labels, cluster_centers, num_clusters]

def getClusterAreas(data):
    step_size = 0.01
    x_min, x_max = data[:,0].min() - 1, data[:,0].max() + 1
    y_min, y_max = data[:,1].min() - 1, data[:,1].max() + 1
    x_vals, y_vals = np.meshgrid(np.arange(x_min, x_max, step_size), np.arange(y_min, y_max, step_size))

    output = ms_model.predict(np.c_[x_vals.ravel(), y_vals.ravel()])
    output = output.reshape(x_vals.shape)

    return [output, x_vals, y_vals]
