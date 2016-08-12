import pandas as pd
import numpy as np
import math
import random
from read_csvfile import read_csvfile
from kmeans_mf_wk import euclidean_distance
from ast import literal_eval

def kNN(data, feature_name, num_dim, new_house, num_neighbors):
    neighbors_list = []
    print("num of houses in this cluster = {}".format(len(data)))
    target_feature_value = new_house.loc[feature_name]
    target_feature_data = data[feature_name]

    distances = []
    for index, row in enumerate(target_feature_data):
        curr_feature_value = row
        distance = euclidean_distance(curr_feature_value, target_feature_value, num_dim)
        # print "({}, {}, {})".format(index, curr_feature_value, distance)
        distances.append([index, distance])
    distances.sort(key=getKey)

    for i in range(num_neighbors):
        item_idx = distances[i][0]
        neighbor = data.iloc[item_idx]
        neighbors_list.append(neighbor)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate', 'cluster', 'feature_vector']
    neighbors = pd.DataFrame(neighbors_list, columns = header)
    neighbors = neighbors.sort_values(by=[feature_name], ascending=[True])
    return neighbors

def getKey(item):
    return item[1]

def main():
    city = 'san-francisco-ca'

    '''
        To use 1-Feature
    '''
    # filename = 'data/clustered_results/{}.csv'.format(city)
    # header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate', 'cluster']
    # feature_name = 'zestimate'
    # num_dim = 1

    '''
        To use multi-Feature
    '''
    filename = 'data/clustered_results/{}_2f.csv'.format(city)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate', 'cluster', 'feature_vector']
    feature_name = 'feature_vector'
    num_dim = 2

    data = read_csvfile(filename, header)
    if feature_name == 'feature_vector':
        for i in range(len(data)):
            data['feature_vector'].iloc[i] = literal_eval(data['feature_vector'].iloc[i])

    # pick random house
    random_idx= random.randrange(0, len(data))
    new_house = data.iloc[random_idx]
    print("---- House Picked -----")
    print(new_house)

    num_neighbors = 10
    neighbors = kNN(data, feature_name, num_dim, new_house, num_neighbors)
    print("---- {} Neighbors ----".format(num_neighbors))
    print(neighbors)

if __name__ == '__main__':
    main()
