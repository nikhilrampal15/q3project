import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import math
from read_csvfile import read_csvfile
from kmeans_1f_wk import kmeans_1f
from kNN_wk import kNN

def find_nearest_cluster(item, centroids):
    min_distance = float('inf')
    for idx, centroid in enumerate(centroids):
        euclidean_distance = math.sqrt(math.pow((centroid - item), 2))
        if euclidean_distance < min_distance:
            min_distance = euclidean_distance
            cluster_idx = idx
    return cluster_idx

def find_similar_houses(data, feature_name, centroids, new_house, num_neighbors):
    new_zestimate = new_house.loc[feature_name]
    print("target zestimate = {}".format(new_zestimate))
    cluster_idx = find_nearest_cluster(new_zestimate, centroids)
    print("target cluster = {}".format(cluster_idx))
    target_cluster_data = data.loc[data['cluster'] == cluster_idx]

    neighbors = kNN(target_cluster_data, feature_name, new_house, num_neighbors)
    return neighbors

def main():
    city = "santa-clara-ca"
    k = 3
    feature_name = 'zestimate'
    threshold_pct = 0.1
    num_neighbors = 10

    filename = "data/propertyInfo/{}.csv".format(city)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate']
    data = read_csvfile(filename, header)
    data['cluster'] = -1 # add new column to indicate cluster
    # print data.head(5)

    # Clustering using k-means Algorithm
    print("------- Clustering by {} --------".format(feature_name))
    centroids = kmeans_1f(data, k, feature_name, threshold_pct)

    # print("****** Resulting Cluster ******")
    # bycluster = data.groupby(['cluster'])
    # print(bycluster[feature_name].describe())

    # Find similar houses using k-NN Algorithm
    random_idx= random.randrange(0, len(data))
    new_house = data.iloc[random_idx]
    print("---- House Picked -----")
    print(new_house)
    print("------- Recommend {} houses --------".format(num_neighbors))
    recommended_houses = find_similar_houses(data, feature_name, centroids, new_house, num_neighbors)
    print(recommended_houses)

    write_fname = "data/clustered_results/{}.csv".format(city)
    write_to_csvfile(data, write_fname)


def write_to_csvfile(data, fname):
    data.to_csv(fname, index=False)
    return


if __name__ == '__main__':
    main()
