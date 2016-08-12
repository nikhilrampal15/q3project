import pandas as pd
import numpy as np
import math
import random
from read_csvfile import read_csvfile
from kmeans_wk import euclidean_distance

def kNN(data, feature_names, num_dim, query_item, num_neighbors):
    neighbors_list = []

    target_feature_values = []
    for name in feature_names:
        element = query_item[name]
        target_feature_values.append(element)
    print "target feature values = {}".format(target_feature_values)
    target_feature_data = data[feature_names]

    distances = []
    for index in range(len(target_feature_data)):
        curr_feature_values = target_feature_data.iloc[index]
        distance = euclidean_distance(curr_feature_values, target_feature_values, num_dim)
        distances.append([index, distance])
    distances.sort(key=getKey)

    for i in range(num_neighbors):
        item_idx = distances[i][0]
        neighbor = data.iloc[item_idx]
        neighbors_list.append(neighbor)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate', 'cluster']
    for name in feature_names:
        header.append(name)
    neighbors = pd.DataFrame(neighbors_list, columns = header)
    print neighbors
    neighbors = neighbors.sort_values(by=feature_names[0], ascending=[True])
    return neighbors

def getKey(item):
    return item[1]

def main():
    city = 'san-francisco-ca'
    # feature_names = ['zestimate']
    feature_names = ['sqft', 'zestimate']
    num_dim = len(feature_names)

    filename = 'data/clustered_results/{}_{}f.csv'.format(city, num_dim)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate', 'cluster', 'sqft_norm', 'zestimate_norm']
    data = read_csvfile(filename, header)

    random_idx= random.randrange(0, len(data))
    query_item = data.iloc[random_idx]
    print("---- House Picked -----")
    print(query_item)

    num_neighbors = 10

    normalized_feature_names = []
    for name in feature_names:
        normalized_feature_names.append(name + '_norm')
    neighbors = kNN(data, normalized_feature_names, num_dim, query_item, num_neighbors)
    print("---- {} Neighbors ----".format(num_neighbors))
    print(neighbors)


if __name__ == '__main__':
    main()
