import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import math
from read_csvfile import read_csvfile

def normalize_feature(feature):
    minimum = float(feature.min())
    maximum = float(feature.max())
    median = float(feature.median())
    print("minimum = {}, maximum = {}, median = {}".format(minimum, maximum, median))
    scaling_factor = 1 / median
    feature = feature * scaling_factor
    return feature

def create_feature_vectors(data, feature_names):
    feature_vector_names = []
    for i in range(len(feature_names)):
        feature_name_normalized = feature_names[i] + '_norm'
        data[feature_name_normalized] = normalize_feature(data[feature_names[i]])
        feature_vector_names.append(feature_name_normalized)
    feature_vectors = data[feature_vector_names]
    return feature_vectors

def initialize_centroids(feature_vectors, k, num_dim):
    centroids = []
    while len(centroids) != k:
        idx = random.randint(0, len(feature_vectors))
        centroid = []
        for i in range(num_dim):
            element = feature_vectors.iloc[idx, i]
            centroid.append(element)
        centroids.append(centroid)
    return centroids

def euclidean_distance(x, y, num_dim):
    distance = 0
    if num_dim == 1:
        distance = math.pow( (x - y), 2)
    else:
        for i in range(num_dim):
            distance += math.pow((x[i] - y[i]), 2)
    distance = math.sqrt(distance)
    return distance

def assign_clusters(data, centroids, feature_vectors, num_dim):
    '''Assign clusters to each observation'''
    for data_idx in range(len(feature_vectors)):
        item = feature_vectors.iloc[data_idx]
        min_distance = float('inf')
        for idx, centroid in enumerate(centroids):
            distance = euclidean_distance(centroid, item, num_dim)
            if distance < min_distance:
                min_distance = distance
                cluster_idx = idx
        data.loc[data_idx, 'cluster'] = cluster_idx
    return data

def cal_cluster_mean(feature_vectors):
    cluster_center = []
    for col in range(len(feature_vectors.iloc[0])):
        total = 0
        count = 0
        for row in range(len(feature_vectors)):
            total += float(feature_vectors.iloc[row][col])
            count += 1
        average = total / count
        cluster_center.append(average)
    return cluster_center

def update_centroids(data, k, threshold_pct, orig_centroids, feature_vectors, num_dim):
    '''Update centroids to mean value of each cluster'''
    centroids = []
    for i in range(k):
        curr_cluster_data = data[data.cluster == i]
        feature_vector_names = feature_vectors.dtypes.index
        curr_cluster_feature_vectors = curr_cluster_data[feature_vector_names]
        cluster_center = cal_cluster_mean(curr_cluster_feature_vectors)
        centroids.append(cluster_center)
    print orig_centroids

    count = 0
    for i in range(k):
        thresholds = []
        if num_dim == 1:
            thresholds = orig_centroids[i][0] * threshold_pct
            if euclidean_distance(centroids[i][0], orig_centroids[i][0], num_dim) < thresholds:
                count += 1
        else:
            for j in range(num_dim):
                threshold = orig_centroids[i][j] * threshold_pct
                thresholds.append(threshold)
            if euclidean_distance(centroids[i], orig_centroids[i], num_dim) < euclidean_distance(thresholds, [0] * num_dim, num_dim):
                count += 1
    if count == k:
        return False
    return centroids

def kmeans(data, k, feature_vectors, num_dim, threshold_pct):
    '''k-means algorith for multi-features'''
    centroids = initialize_centroids(feature_vectors, k, num_dim)
    print("Centroids 0 = {}".format(centroids))

    count = 1
    while centroids != False:
        data = assign_clusters(data, centroids, feature_vectors, num_dim)
        orig_centroids = centroids
        centroids = update_centroids(data, k, threshold_pct, orig_centroids, feature_vectors, num_dim)
        print("Centroids {} = {}".format(count, centroids))
        count += 1
    return orig_centroids

def write_to_csvfile(data, fname):
    data.to_csv(fname, index=False, cols=('zpid', 'street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate', 'cluster'))
    return

def main():
    city = "dallas-tx"
    k = 5
    # feature_names = ['zestimate']
    feature_names = ['sqft', 'zestimate']
    num_dim = len(feature_names)
    threshold_pct = 0.1

    filename = "data/propertyInfo/{}.csv".format(city)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate']
    data = read_csvfile(filename, header)
    data['cluster'] = -1

    feature_vectors = create_feature_vectors(data, feature_names)
    print("------- Clustering by {} --------".format(feature_names))
    centroids = kmeans(data, k, feature_vectors, num_dim, threshold_pct)

    write_fname = "data/clustered_results/{}_{}f.csv".format(city, num_dim)
    write_to_csvfile(data, write_fname)

'''
    Main portion of the program
'''
if __name__ == '__main__':
    main()
