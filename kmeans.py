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

def assign_cluster(centroids, data):
    data = data[0:3]
    for item in data:
        min_distance = float('inf')
        print "item = {}".format(item)
        for idx, centroid in enumerate(centroids):
            print "idx = {}, centroid = {}".format(idx, centroid)
            distance = pow((int(centroid) - int(item)), 2)
            if distance < min_distance:
                min_distance = distance
                cluster_idx = idx
                print "cluster_idx = {}".format(cluster_idx)

    return


def kmeans():
    pass

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
