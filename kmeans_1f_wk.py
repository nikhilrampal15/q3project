import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import math
from read_csvfile import read_csvfile

def initialize_centroids(feature, k):
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

def cal_mean_feature(data):
    total = 0
    count = 0
    for item in data:
        if item != 'Unavailable':
            total += int(item)
            count += 1
    return total / count

def assign_cluster(data, centroids, feature_name):
    '''Assign clusters to each observation'''
    feature = data[feature_name]
    for data_idx, item in enumerate(feature):
        min_distance = float('inf')
        for idx, centroid in enumerate(centroids):
            euclidean_distance = math.sqrt(math.pow((centroid - item), 2))
            if euclidean_distance < min_distance:
                min_distance = euclidean_distance
                cluster_idx = idx
        data.loc[data_idx, 'cluster'] = cluster_idx
    return data

def update_centroids(data, k, threshold_pct, orig_centroids, feature_name):
    '''Update centroids to mean value of each cluster'''
    centroids = []
    for i in range(k):
        curr_cluster_list = data[data.cluster == i]
        updated_centroid = cal_mean_feature(curr_cluster_list[feature_name])
        centroids.append(updated_centroid)
    count = 0
    for i in range(k):
        threshold = orig_centroids[i] * threshold_pct
        if math.fabs(centroids[i] - orig_centroids[i]) < threshold:
            count += 1
    if count == k:
        return False
    return centroids

def kmeans_1f(data, k, feature_name, threshold_pct):
    '''k-means algorith for one feature

        Works for zestimate and sqft
        Need threshold adjustment for bedroom and bathroom
        Does not work for non-integer features (zipcode, city and etc)

    '''
    feature = data[feature_name]
    centroids = initialize_centroids(feature, k)
    print("Centroids 0 = {}".format(centroids))

    count = 1
    while centroids != False:
        data = assign_cluster(data, centroids, feature_name)
        orig_centroids = centroids
        centroids = update_centroids(data, k, threshold_pct, orig_centroids, feature_name)
        print("Centroids {} = {}".format(count, centroids))
        count += 1
    return data

'''
    Main portion of the program
'''
if __name__ == '__main__':
    city = "redwood-city-ca"
    k = 3
    feature_name = 'zestimate'
    threshold_pct = 0.001

    filename = "data/propertyInfo/{}.csv".format(city)
    data = read_csvfile(filename)
    data['cluster'] = -1 # add new column to indicate cluster
    # print("# of rows = {}".format(len(data)))
    # print data.head(5)

    print("------- Clustering by {} --------".format(feature_name))
    clustered_data = kmeans_1f(data, k, feature_name, threshold_pct)

    print("****** Resulting Cluster ******")
    bycluster = clustered_data.groupby(['cluster'])
    print(bycluster[feature_name].describe())
