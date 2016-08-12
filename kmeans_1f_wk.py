import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import math
from read_csvfile import read_csvfile
from kmeans_mf_wk import euclidean_distance

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

def cal_cluster_mean(data):
    total = 0
    count = 0
    for item in data:
        # if item != 'Unavailable':
        total += int(item)
        count += 1
    return total / count

def assign_clusters(data, centroids, feature_name, num_dim):
    '''Assign clusters to each observation'''
    feature = data[feature_name]
    for data_idx, item in enumerate(feature):
        min_distance = float('inf')
        for idx, centroid in enumerate(centroids):
            distance = euclidean_distance(centroid, item, num_dim)
            if distance < min_distance:
                min_distance = distance
                cluster_idx = idx
        data.loc[data_idx, 'cluster'] = cluster_idx
    return data

def update_centroids(data, k, threshold_pct, orig_centroids, feature_name):
    '''Update centroids to mean value of each cluster'''
    centroids = []
    for i in range(k):
        curr_cluster_list = data[data.cluster == i]
        updated_centroid = cal_cluster_mean(curr_cluster_list[feature_name])
        centroids.append(updated_centroid)
    count = 0
    for i in range(k):
        threshold = orig_centroids[i] * threshold_pct
        # if math.fabs(centroids[i] - orig_centroids[i]) == 0:
        #     count += 1
        if math.fabs(centroids[i] - orig_centroids[i]) < threshold:
            count += 1
    if count == k:
        return False
    return centroids

def kmeans_1f(data, k, feature_name, num_dim, threshold_pct):
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
        data = assign_clusters(data, centroids, feature_name, num_dim)
        orig_centroids = centroids
        centroids = update_centroids(data, k, threshold_pct, orig_centroids, feature_name)
        print("Centroids {} = {}".format(count, centroids))
        count += 1
    return orig_centroids

def main():
    city = "san-francisco-ca"
    k = 3
    feature_name = ['zestimate']
    num_dim = len(feature_name)
    threshold_pct = 0.01

    filename = "data/propertyInfo/{}.csv".format(city)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate']
    data = read_csvfile(filename, header)
    data['cluster'] = -1 # add new column to indicate cluster
    # print("# of rows = {}".format(len(data)))
    # print data.head(5)

    print("------- Clustering by {} --------".format(feature_name))
    centroids = kmeans_1f(data, k, feature_name[0], num_dim, threshold_pct)
    print centroids

    print("****** Resulting Cluster ******")
    bycluster = data.groupby(['cluster'])
    print(bycluster[feature_name[0]].describe())

'''
    Main portion of the program
'''
if __name__ == '__main__':
    main()
