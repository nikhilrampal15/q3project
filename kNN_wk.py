import pandas as pd
import numpy as np
import math
import random
from read_csvfile import read_csvfile
from kmeans_mf_wk import euclidean_distance
from ast import literal_eval

def kNN(data, feature_name, new_house, num_neighbors):
    neighbors_list = []
    print("num of houses in this cluster = {}".format(len(data)))
    target_feature_value = new_house.loc[feature_name]
    target_feature_data = data[feature_name]

    distances = []
    for index, row in enumerate(target_feature_data):
        curr_feature_value = row
        distance = euclidean_distance(curr_feature_value, target_feature_value)
        # distance = math.sqrt(math.pow((curr_feature_value - target_feature_value), 2))
        # print "({}, {}, {})".format(index, curr_feature_value, distance)
        distances.append([index, distance])
    distances.sort(key=getKey)

    for i in range(num_neighbors):
        item_idx = distances[i][0]
        neighbor = data.iloc[item_idx]
        neighbors_list.append(neighbor)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate']
    neighbors = pd.DataFrame(neighbors_list, columns = header)
    neighbors = neighbors.sort_values(by=['zestimate'], ascending=[True])
    return neighbors

def getKey(item):
    return item[1]

def main():
    city = 'san-francisco-ca'
    # filename = 'data/propertyInfo/{}.csv'.format(city)
    # header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate']
    # feature_name = 'zestimate'
    filename = 'data/clustered_results/{}_2f.csv'.format(city)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate', 'feature_vector']
    feature_name = 'feature_vector'

    data = read_csvfile(filename, header)
    if feature_name == 'feature_vector':
        data['feature_name'] = literal_eval(data['feature_name'])

    # pick random house
    random_idx= random.randrange(0, len(data))
    new_house = data.iloc[random_idx]
    print("---- House Picked -----")
    print(new_house)

    num_neighbors = 10
    neighbors = kNN(data, feature_name, new_house, num_neighbors)
    print("---- {} Neighbors ----".format(num_neighbors))
    print(neighbors)

if __name__ == '__main__':
    main()
