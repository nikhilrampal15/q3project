import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import math
from read_csvfile import read_csvfile
from kmeans_1f_wk import kmeans_1f
from kmeans_mf_wk import kmeans_mf
from kmeans_mf_wk import euclidean_distance
from kmeans_mf_wk import create_feature_vectors
from kNN_wk import kNN

def find_nearest_cluster(item, centroids, num_dim):
    min_distance = float('inf')
    for idx, centroid in enumerate(centroids):
        distance = euclidean_distance(centroid, item, num_dim)
        if distance < min_distance:
            min_distance = distance
            cluster_idx = idx
    return cluster_idx

def find_similar_houses(data, feature_name, num_dim, centroids, new_house, num_neighbors):
    target_feature_value = new_house.loc[feature_name]
    print("target {} value = {}".format(feature_name, target_feature_value))
    cluster_idx = find_nearest_cluster(target_feature_value, centroids, num_dim)
    print("target cluster = {}".format(cluster_idx))
    target_cluster_data = data.loc[data['cluster'] == cluster_idx]

    neighbors = kNN(target_cluster_data, feature_name, num_dim, new_house, num_neighbors)
    return neighbors

def write_to_csvfile(data, fname):
    data.to_csv(fname, index=False)
    return

def main():
    city = "All-houses"
    k = 5
    threshold_pct = 0.1
    num_neighbors = 10

    filename = "data/propertyInfo/{}.csv".format(city)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate']
    data = read_csvfile(filename, header)
    data['cluster'] = -1 # add new column to indicate cluster
    # print data.head(5)

    feature_names = ['zestimate']
    # feature_names = ['sqft', 'zestimate']
    num_dim = len(feature_names)
    # Clustering using k-means Algorithm
    print("------- Clustering by {} --------".format(feature_names))

    '''
        To use 1-Feature
    '''
    centroids = kmeans_1f(data, k, feature_names[0], num_dim, threshold_pct)
    # Find similar houses using k-NN Algorithm
    random_idx= random.randrange(0, len(data))
    random_idx = 8809
    new_house = data.iloc[random_idx]
    print("---- House Picked -----")
    print(new_house)
    print("------- Recommend {} houses --------".format(num_neighbors))
    recommended_houses = find_similar_houses(data, feature_names[0], num_dim, centroids, new_house, num_neighbors)
    print(recommended_houses)


    '''
        To use multi-Feature
    '''
    # feature_vectors = create_feature_vectors(data, feature_names)
    # centroids = kmeans_mf(data, k, feature_vectors, num_dim, threshold_pct)
    # # Find similar houses using k-NN Algorithm
    # random_idx= random.randrange(0, len(data))
    # random_idx = 8809
    # new_house = data.iloc[random_idx]
    # print("---- House Picked -----")
    # print(new_house)
    # print("------- Recommend {} houses --------".format(num_neighbors))
    # recommended_houses = find_similar_houses(data, 'feature_vector', num_dim, centroids, new_house, num_neighbors)
    # print(recommended_houses)

    write_fname = 'data/clustered_results/{}_{}f.csv'.format(city, num_dim)
    write_to_csvfile(data, write_fname)


if __name__ == '__main__':
    main()
