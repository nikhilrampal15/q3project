import pandas as pd
import numpy as np
import random
from read_csvfile import read_csvfile
k = 5
city = "san-francisco-ca"
filename = "data/propertyInfo/{}.csv".format(city)
data = read_csvfile(filename)
data["cluster"] = -1
# print(data)
# print(data['zestimate'].dtype)

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

import copy
def cluster(centroids, house_data):
    shortest_distance = []
    # create an list that compares distance from centeroid to house
    pass
    houses = house_data['zestimate']
    for x in range(len(centroids)):
        # loop from 0 to 5
        centroid = centroids[x]
        #print(type(centroid))
        #print(centroid)
        # print(houses)
        for idx, y in enumerate(houses):
                offset = len(houses) * x
                #print(idx, len(houses))
                home = houses[idx]
                if home > centroid:
                    shortest_distance.append([home-centroid, centroid, y])
                    house_data.loc[idx + offset, 'cluster'] = centroid

            # adds distance to list along with centroid location
                else:
                    shortest_distance.append([centroid-home, centroid, y])
                    house_data.loc[idx + offset, 'cluster'] = centroid
    shortest_distance.sort(key=lambda a: a[0])
    # sorts zeroth index of list inside list which is the distance
    """
    here we create the convergence method
    """


    shortest_distance.sort(key=lambda a: a[1])
    # for i in shortest_distance:
    #     centroid_sort = shortest_distance.sort(key=lambda a: a[1])
    return shortest_distance
    # returns the cluster that is closest to the home






answer = centroids(data)
#print(answer)
cluster(answer, data)
#print(data)

# for item in myData:
# print(item)
#print(data)
print(data['cluster'])
# for item in data['cluster']:
#     print(item)

pd.set_option('display.max_rows', len(data['zestimate']))
x = data['zestimate']
#print (x)
pd.set_option('display.float_format', lambda x: '%.0f' % x)
#print (x)
print('hello')
#print(data['zestimate'])