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
    # scaling_factor = 1 / (maximum - minimum)
    scaling_factor = 1 / median
    # print float(scaling_factor)
    feature = feature * scaling_factor
    return feature

def create_feature_vectors(data, feature_names):
    for i in range(len(feature_names)):
        feature_name_normalized = feature_names[i] + '_norm'
        data[feature_name_normalized] = normalize_feature(data[feature_names[i]])
    data['feature_vector'] = pd.Series(dtype='object')
    for i in range(len(data)):
        features = [data.loc[i, 'sqft_norm'], data.loc[i, 'zestimate_norm']]
        data.set_value(i, 'feature_vector', features)
    feature_vectors = data['feature_vector']
    return feature_vectors

def initialize_centroids(feature_vectors, k):
    centroids = []
    while len(centroids) != k:
        idx = random.randint(0, len(feature_vectors))
        centroid = feature_vectors.iloc[idx]
        centroids.append(centroid)
    return centroids

def cal_feature_mean(data):
    total = 0
    count = 0
    for item in data:
        if item != 'Unavailable':
            total += int(item)
            count += 1
    return total / count

def euclidean_distance(x, y):
    distance = 0
    n_dimension = len(x)
    for i in range(n_dimension):
        distance += math.pow((x[i] - y[i]), 2)
    distance = math.sqrt(distance)
    return distance

def assign_clusters(data, centroids, feature_vectors):
    '''Assign clusters to each observation'''
    for data_idx, item in enumerate(feature_vectors):
        min_distance = float('inf')
        for idx, centroid in enumerate(centroids):
            distance = euclidean_distance(centroid, item)
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
        updated_centroid = cal_feature_mean(curr_cluster_list[feature_name])
        centroids.append(updated_centroid)
    count = 0
    for i in range(k):
        threshold = orig_centroids[i] * threshold_pct
        if math.fabs(centroids[i] - orig_centroids[i]) < threshold:
            count += 1
    if count == k:
        return False
    return centroids

def kmeans_mf(data, k, feature_vectors, threshold_pct):
    '''k-means algorith for multi-features'''
    centroids = initialize_centroids(feature_vectors, k)
    print("Centroids 0 = {}".format(centroids))

    data = assign_clusters(data, centroids, feature_vectors)
    # count = 1
    # while centroids != False:
    #     data = assign_clusters(data, centroids, feature_name)
    #     orig_centroids = centroids
    #     centroids = update_centroids(data, k, threshold_pct, orig_centroids, feature_name)
    #     print("Centroids {} = {}".format(count, centroids))
    #     count += 1
    # return orig_centroids
    return

def main():
    city = "san-francisco-ca"
    k = 3
    feature_names = ['sqft', 'zestimate']
    threshold_pct = 0.01

    filename = "data/propertyInfo/{}.csv".format(city)
    data = read_csvfile(filename)
    data['cluster'] = -1 # add new column to indicate cluster

    # generate feature vectors columns
    feature_vectors = create_feature_vectors(data, feature_names)

    print("------- Clustering by {} --------".format(feature_vectors))
    centroids = kmeans_mf(data, k, feature_vectors, threshold_pct)
    print centroids

    # print("****** Resulting Cluster ******")
    # bycluster = data.groupby(['cluster'])
    # print(bycluster[feature_name].describe())

'''
    Main portion of the program
'''
if __name__ == '__main__':
    main()
