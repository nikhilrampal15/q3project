import pandas as pd
import numpy as np
import random

k = 5
city = "redwood-city-ca"
filename = "data/propertyInfo/{}.csv".format(city)
header = ['zpid', 'street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate']
house = pd.read_csv(filename, sep='\t', names=header)
house = house.replace('Unavailable', np.NaN)
house_no_missing = house.dropna()


def centroids(house_data):
    # takes in housing data parameter
    centroid = []
    pass
    for x in range(k):
        # loop from 0 to 5
        centroid.append(random.randint(1, len(house_data)))
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
        for y in house_data:
            houses = house_data[y]
            for z in houses:
                home = np.asscalar(houses[z])
                if home > centroid:
                    shortest_distance.append([home-centroid**2, centroid])
            # adds RMSE distance to list along with centroid location
                else:
                    shortest_distance.append([centroid-home**2, centroid])
    shortest_distance.sort(key=lambda a: a[0])
    # sorts zeroth index of list inside list which is the distance
    return shortest_distance[0][1]
    # returns the cluster that is closest to the home


if __name__ == '__main__':
    print(cluster(centroids(house), house))
    #print(centroids(house))
    #print (house)
