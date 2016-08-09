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
    centroids = set()
    while len(centroids) != k:
        centroid = random.choice(feature)
        centroids.add(centroid)
    return list(centroids)

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

def update_centroid(data, k):
    centroids = set()
    for i in range(k):
        curr_cluster_list = data[data.cluster == i]
        updated_centroid = cal_mean_zestimate(curr_cluster_list['zestimate'])
        centroids.add(updated_centroid)
    return list(centroids)


if __name__ == '__main__':
    city = "redwood-city-ca"
    filename = "data/propertyInfo/{}.csv".format(city)
    data = read_csvfile(filename)
    data['cluster'] = -1 # add new column to indicate cluster
    print("# of rows = {}".format(len(data)))
    print("Initial data")
    # print data.head(5)

    k = 3
    feature = data['zestimate']
    centroids = initialize_centroid(feature, k)
    print("\nInitial Centroids = {}".format(centroids))

    count = 1
    while count <= 3:
        data = assign_cluster(centroids, data)
        print("After cluster assignment")
        print(data.head(5))
        bycluster = data.groupby(['cluster'])
        print(bycluster['zestimate'].describe())

        centroids = update_centroid(data, k)
        print("Centroids {} = {}".format(count, centroids))
        count += 1
