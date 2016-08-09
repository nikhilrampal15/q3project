import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
# Workaround of an error: Python is not installed as a framework
import random
k=5
def centroids(house_data):
    #takes in housing data parameter
    centroid = []
    pass
    for x in range(k):
        #loop from 0 to 5
        centroid.append(random.randint(1,len(house_data)))
        #adds a random integer to the list
    return centroid
    #return the array of random points

def cluster(centroids,house_data):
    shortest_distance =[]
    #create an list that compares distance from centeroid to house
    pass
    for x in range(k):
        #loop from 0 to 5
        houses = house_data[x]
        centroid = centroids[x]
        if houses > centroid:
            shortest_distance.append([houses-centroids**2,centroids])
            #adds RMSE distance to list along with centroid location
        else:
            shortest_distance.append([centroids-houses**2,centroids])
    shortest_distance.sort(key=lambda z: z[0])
    #sorts zeroth index of list inside list which is the distance
    return shortest_distance[0][1]
    #returns the cluster that is closest to the home


if __name__ == '__main__':
    city = "redwood-city-ca"
    filename = "data/propertyInfo/{}.csv".format(city)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate']
    house = pd.read_csv(filename, sep='\t', names=header)
    house = house.replace('Unavailable', np.NaN)
    house_no_missing = house.dropna()
    print house_no_missing.head(3)
    zestimate = house_no_missing['zestimate']

    k = 3
    centroids = initialize_centroid(zestimate, k)
    print centroids
    assign_cluster(centroids, zestimate)
