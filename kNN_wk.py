import pandas as pd
import numpy as np
import math
import random
from read_csvfile import read_csvfile
from kmeans_mf_wk import euclidean_distance
from ast import literal_eval

def kNN(data, feature_names, num_dim, new_house, num_neighbors):
    neighbors_list = []
    print("num of houses in this cluster = {}".format(len(data)))

    target_feature_values = []
    for name in feature_names:
        element = new_house[name]
        target_feature_values.append(element)
    print "target feature values = {}".format(target_feature_values)
    target_feature_data = data[feature_names]

    distances = []
    for index in range(len(target_feature_data)):
        curr_feature_values = target_feature_data.iloc[index]
        distance = euclidean_distance(curr_feature_values, target_feature_values, num_dim)
        # print "({}, {}, {})".format(index, curr_feature_value, distance)
        distances.append([index, distance])
    distances.sort(key=getKey)

    for i in range(num_neighbors):
        item_idx = distances[i][0]
        neighbor = data.iloc[item_idx]
        neighbors_list.append(neighbor)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate', 'cluster', 'sqft_norm', 'zestimate_norm']
    neighbors = pd.DataFrame(neighbors_list, columns = header)
    neighbors = neighbors.sort_values(by=feature_names[0], ascending=[True])
    return neighbors

def getKey(item):
    return item[1]

def main():
    city = 'san-francisco-ca'

    # feature_names = ['zestimate']
    feature_names = ['sqft_norm', 'zestimate_norm']
    num_dim = len(feature_names)

    filename = 'data/clustered_results/{}_{}f.csv'.format(city, num_dim)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate', 'cluster', 'sqft_norm', 'zestimate_norm']
    data = read_csvfile(filename, header)

    # pick random house
    random_idx= random.randrange(0, len(data))
    new_house = data.iloc[random_idx]
    print("---- House Picked -----")
    print(new_house)

    num_neighbors = 10
    neighbors = kNN(data, feature_names, num_dim, new_house, num_neighbors)
    print("---- {} Neighbors ----".format(num_neighbors))
    print(neighbors)

if __name__ == '__main__':
    main()
