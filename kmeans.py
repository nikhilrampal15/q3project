"""
K-Means Algorithm Implementation
"""

import pandas as pd
import numpy as np
import random
from read_csvfile import read_csvfile
import math
import functools

"""
Data-Set Information
"""

city = "san-francisco-ca"
filename = "data/propertyInfo/{}.csv".format(city)
data = read_csvfile(filename)
data["cluster"] = -1

"""
Generating Centroids
"""


# amount of centroids chosen


def centroids(house_data,k,column_name):
    # takes in housing data parameter
    #value of amount of centroids to be created
    centroid = []
    # create list to add random centroids
    pass
    for x in range(k):
        # loop from 0 to 5
        centroid.append(random.randint(1,house_data[column_name].max()))
        # adds a random integer to the list
    return centroid
    # return the array of random points


list_of_centroids = centroids(data, 5,'zestimate')


# easier to store function call in a variable

"""
Use list of centroids to create clusters of homes
"""


def cluster(centroids, house_data, column_name):
    shortest_distance = []
    # create an list that compares distance from centeroid to house

    # new centroids to compare to original
    houses = house_data[column_name]
    # grabs the data table at column 'zestimate' or a different parameter
    for x in range(len(centroids)):
        # loop from 0 to 5
        centroid = centroids[x]
        new_centroids = []
        # iterating through the list of centroids and locating each individual centroid
        for idx, y in enumerate(houses):
                offset = len(houses) * x
                # print(idx, len(houses))
                home = houses[idx]
                homee = np.asscalar(home.astype(int))
                # home is located at a specific index
                shortest_distance.append([math.sqrt(abs(homee-centroid)**2), centroid, y])
                # add to the list an array with euclidean distance,centroid number,initial value

                #print(type(homee))

                distance = math.sqrt(abs(homee-centroid)**2)

                new_centroids.append(distance)

                house_data.loc[idx + offset, 'cluster'] = centroid
                # update the cell with new cluster value in dataset
        sum_of_centroid = [sum(new_centroids)]
        print(sum_of_centroid)
    shortest_distance.sort(key=lambda a: a[0])
    # sorts zeroth index of list inside list which is the distance
    return shortest_distance[0]
    # returns the cluster that is closest to the home

"""
    Here we create the convergence method
"""

 # def convergence(list_of_centroids,k):
 #     k = 5
 #     homes_in_cluster = [data.cluster]
 #     new_centroid = []
 #     for i in range(k):
 #         if[data.cluster == i]:





cluster(list_of_centroids, data,'zestimate')
#print(data)

# for item in myData:
# print(item)
#print([data.cluster])
#print(data['cluster'])
# for item in data['cluster']:
#     print(item)

#convergence(list_of_centroids)
#print([data.cluster])

pd.set_option('display.max_rows', len(data['zestimate']))
x = data['zestimate']
#print (x)
pd.set_option('display.float_format', lambda x: '%.0f' % x)
#print (x)
#print(data['zestimate'])