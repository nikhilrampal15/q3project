import pandas as pd
import numpy as np
import math
import random
from read_csvfile import read_csvfile

def kNN(data, feature_name, new_house, num_neighbors):
    neighbors_list = []
    print("num of houses in this cluster = {}".format(len(data)))
    new_zestimate = new_house.loc[feature_name]
    zestimate_data = data[feature_name]

    distances = []
    for index, row in enumerate(zestimate_data):
        curr_zestimate = row
        euclidean_distance = math.sqrt(math.pow((curr_zestimate - new_zestimate), 2))
        # print "({}, {}, {})".format(index, curr_zestimate, euclidean_distance)
        distances.append([index, euclidean_distance])
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
    filename = 'data/clustered_results/{}_2f.csv'.format(city)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate', 'feature_vector']
    data = read_csvfile(filename, header)
    feature_name = 'zestimate'
    print data

    # pick random house
    random_idx= random.randrange(0, len(data))
    new_house = data.iloc[random_idx]
    print("---- House Picked -----")
    print(new_house)

    # num_neighbors = 10
    # neighbors = kNN(data, feature_name, new_house, num_neighbors)
    # print("---- {} Neighbors ----".format(num_neighbors))
    # print(neighbors)

if __name__ == '__main__':
    main()
