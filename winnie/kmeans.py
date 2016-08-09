import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg') # Workaround of an error: Python is not installed as a framework
from sets import Set
import random

def initialize_centroid(data, k):
    centroids = Set()
    while len(centroids) != k:
        centroid = random.choice(data)
        centroids.add(centroid)
    return list(centroids)

def assign_cluster(centroids, house):
    zestimate = house['zestimate']
    for item in zestimate:
        min_distance = float('inf')
        for idx, centroid in enumerate(centroids):
            distance = pow((int(centroid) - int(item)), 2)
            if distance < min_distance:
                min_distance = distance
                cluster_idx = idx
        # print "item = {}, cluster_idx = {}".format(item, cluster_idx)
        house['cluster'] = cluster_idx
    return


def kmeans():
    pass

if __name__ == '__main__':
    city = "redwood-city-ca"
    filename = "../data/propertyInfo/{}.csv".format(city)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate']
    house = pd.read_csv(filename, sep='\t', names=header)
    # house = house.set_index('zpid') # use zpid as index
    house = house.replace('Unavailable', np.NaN)
    house['cluster'] = -1 # add new column to indicate cluster
    house = house.dropna() # drop rows with NaN entry
    print house.head(3)

    k = 3
    zestimate = house['zestimate']
    # print zestimate[15565842]

    centroids = initialize_centroid(zestimate, k)
    print centroids

    assign_cluster(centroids, house)
    # print house['cluster']
