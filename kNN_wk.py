import pandas as pd
import numpy as np
import math
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
    filename = 'data/propertyInfo/{}.csv'.format(city)
    data = read_csvfile(filename)
    feature_name = 'zestimate'
    # new_house = pd.DataFrame.from_dict({'zpid': '16948197',
    #                           'street': '4129 Middlesex Dr',
    #                           'city':'San Diego',
    #                           'state':'CA',
    #                           'zipcode':'92116',
    #                           'bedroom': 3,
    #                           'bathroom': 3,
    #                           'sqft': 1750,
    #                           'zestimate': 976980}, orient = 'index')

    new_house = pd.DataFrame.from_dict({'zpid': '15184786',
                              'street': '60 College Ave',
                              'city':'San Francisco',
                              'state':'CA',
                              'zipcode':'94112',
                              'bedroom': 3,
                              'bathroom': 4,
                              'sqft': 1620,
                              'zestimate': 1100651}, orient = 'index')

    num_neighbors = 10
    neighbors = kNN(data, feature_name, new_house, num_neighbors)
    print neighbors

if __name__ == '__main__':
    main()
