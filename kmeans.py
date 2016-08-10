import pandas as pd
import numpy as np
import random
from read_csvfile import read_csvfile
k = 5
city = "san-jose-ca"
filename = "data/propertyInfo/{}.csv".format(city)
data = read_csvfile(filename)
#print(data)
#print(data['zestimate'].dtype)

def centroids(house_data):
    # takes in housing data parameter
    centroid = []
    pass
    for x in range(k):
        # loop from 0 to 5
        centroid.append(random.randint(1,house_data['zestimate'].max()))
        # adds a random integer to the list
    return centroid
    # return the array of random points

def cluster(centroids, house_data):
    shortest_distance = []
    # create an list that compares distance from centeroid to house
    pass
    for x in range(len(centroids)):
        # loop from 0 to 5
        centroid = centroids[x]
        #print(centroids[x])
        houses = house_data['zestimate']
        #print(houses)
        for idx, z in enumerate(houses):
                #print(idx, z)
                home = houses[idx]
                if home > centroid:
                    shortest_distance.append([home-centroid, centroid])
            # adds RMSE distance to list along with centroid location
                else:
                    shortest_distance.append([centroid-home, centroid])
    shortest_distance.sort(key=lambda a: a[0])
    # sorts zeroth index of list inside list which is the distance
    return shortest_distance[0]
    # returns the cluster that is closest to the home
answer = centroids(data)
print(answer)
print(cluster(answer, data))
