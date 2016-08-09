import pandas as pd
import numpy as np
import matplotlib
# matplotlib.use('TkAgg')
# Workaround of an error: Python is not installed as a framework
import random
import math
from read_csvfile import read_csvfile
from read_csvfile import cal_mean_zestimate

def initialize_centroid(feature, k):
    '''Initialize cluster centroids

    Args:
        feature (pandas DataFrame column)
        k (int): number of clusters
    Returns:
        centroids (list)

    '''
    centroids = set() # Use set to prevent duplicates
    while len(centroids) != k:
        centroid = random.choice(feature)
        centroids.add(centroid)
    return sorted(list(centroids))

def assign_cluster(centroids, data):
    '''Assign clusters to each observation

    Args:
        centroids (pandas Series?): list of cluster centroids
        data (?)
    Returns:
        cluster_index (?): cluster index for each observation

    '''
    zestimate = data['zestimate']
    for data_idx, item in enumerate(zestimate):
        min_distance = float('inf')
        for idx, centroid in enumerate(centroids):
            euclidean_distance = math.sqrt(math.pow((centroid - item), 2))
            if euclidean_distance < min_distance:
                min_distance = euclidean_distance
                cluster_idx = idx
        data.loc[data_idx, 'cluster'] = cluster_idx
    return data

def update_centroid(data, k, threshold_pct, orig_centroids):
    centroids = []
    for i in range(k):
        curr_cluster_list = data[data.cluster == i]
        updated_centroid = cal_mean_zestimate(curr_cluster_list['zestimate'])
        centroids.append(updated_centroid)
    count = 0
    for i in range(k):
        threshold = orig_centroids[i] * threshold_pct
        if math.fabs(centroids[i] - orig_centroids[i]) < threshold:
            count += 1
    if count == k:
        return False
    return centroids

if __name__ == '__main__':
    city = "redwood-city-ca"
    filename = "data/propertyInfo/{}.csv".format(city)
    data = read_csvfile(filename)
    data['cluster'] = -1 # add new column to indicate cluster
    print("# of rows = {}".format(len(data)))
    # print data.head(5)
    feature_name = 'zestimate'

    k = 3
    feature = data[feature_name]
    centroids = initialize_centroid(feature, k)
    print("Centroids 0 = {}".format(centroids))

    threshold_pct = 0.01
    count = 1
    while centroids != False:
        data = assign_cluster(centroids, data)
        orig_centroids = centroids
        centroids = update_centroid(data, k, threshold_pct, orig_centroids)
        print("Centroids {} = {}".format(count, centroids))
        count += 1

    print("***Resulting Cluster***")
    bycluster = data.groupby(['cluster'])
    print(bycluster['zestimate'].describe())
