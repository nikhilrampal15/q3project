import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import math
from read_csvfile import read_csvfile
from kmeans_mf_wk import kmeans_mf
from kmeans_mf_wk import create_feature_vectors
from kNN_wk import kNN

def find_nearest_cluster(item, centroids):
    min_distance = float('inf')
    for idx, centroid in enumerate(centroids):
        euclidean_distance = math.sqrt(math.pow((centroid - item), 2))
        if euclidean_distance < min_distance:
            min_distance = euclidean_distance
            cluster_idx = idx
    return cluster_idx

def find_similar_houses(data, feature_vectors, centroids, new_house, num_neighbors):
    new_zestimate = new_house.loc[feature_name]
    print("target zestimate = {}".format(new_zestimate))
    cluster_idx = find_nearest_cluster(new_zestimate, centroids)
    print("target cluster = {}".format(cluster_idx))
    target_cluster_data = data.loc[data['cluster'] == cluster_idx]

    neighbors = kNN(target_cluster_data, feature_name, new_house, num_neighbors)
    return neighbors

def main():
    city = "san-francisco-ca"
    k = 5
    feature_names = ['sqft', 'zestimate']
    threshold_pct = 0.01
    num_neighbors = 10

    filename = "data/propertyInfo/{}.csv".format(city)
    data = read_csvfile(filename)
    data['cluster'] = -1 # add new column to indicate cluster

    # generate feature vectors columns
    feature_vectors = create_feature_vectors(data, feature_names)
    print("------- Clustering by {} --------".format(feature_names))
    centroids = kmeans_mf(data, k, feature_vectors, threshold_pct)

    # Find similar houses using k-NN Algorithm
    random_idx= random.randrange(0, len(data))
    new_house = data.iloc[random_idx]
    print("---- House Picked -----")
    print(new_house)
    print("------- Recommend {} houses --------".format(num_neighbors))
    recommended_houses = find_similar_houses(data, feature_vectors, centroids, new_house, num_neighbors)
    print(recommended_houses)

    write_fname = "data/clustered_results/{}_2f.csv".format(city)
    col_names = ['zpid', 'street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate', 'cluster']
    data1 = data[col_names]
    write_to_csvfile(data1, write_fname, col_names)


def write_to_csvfile(data, fname, col_names):
    data.to_csv(fname, index=False, cols=('zpid', 'street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate', 'cluster'))
    return


if __name__ == '__main__':
    main()
