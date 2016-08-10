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
    city = "All-houses"
    k = 5
    feature_name = 'zestimate'
    threshold_pct = 0.1
    num_neighbors = 10
    # new_house = pd.DataFrame.from_dict({'zpid': '16948197',
    #                           'street': '4129 Middlesex Dr',
    #                           'city':'San Diego',
    #                           'state':'CA',
    #                           'zipcode':'92116',
    #                           'bedroom': 3,
    #                           'bathroom': 3,
    #                           'sqft': 1750,
    #                           'zestimate': 976980}, orient = 'index')
    new_house = pd.DataFrame.from_dict({'zpid': '25403548',
                              'street': '7943 E Altair Ln',
                              'city':'Anaheim',
                              'state':'CA',
                              'zipcode':'92808',
                              'bedroom': 3,
                              'bathroom': 2,
                              'sqft': 1457,
                              'zestimate': 647616}, orient = 'index')

    # print new_house
    # print new_house.loc['zestimate']

    filename = "data/propertyInfo/{}.csv".format(city)
    data = read_csvfile(filename)
    data['cluster'] = -1 # add new column to indicate cluster
    # print data.head(5)

    # Clustering using k-means Algorithm
    print("------- Clustering by {} --------".format(feature_name))
    centroids = kmeans_1f(data, k, feature_name, threshold_pct)

    # print("****** Resulting Cluster ******")
    # bycluster = data.groupby(['cluster'])
    # print(bycluster[feature_name].describe())

    # Find houses using k-NN Algorithm
    print("------- Recommend {} houses --------".format(num_neighbors))
    recommended_houses = find_similar_houses(data, feature_name, centroids, new_house, num_neighbors)
    print(recommended_houses)


if __name__ == '__main__':
    main()
