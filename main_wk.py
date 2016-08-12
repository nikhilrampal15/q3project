import pandas as pd
import numpy as np
import random
import math
from read_csvfile import read_csvfile
from kmeans_wk import kmeans_mf
from kmeans_wk import euclidean_distance
from kmeans_wk import create_feature_vectors
from kNN_wk import kNN

def write_to_csvfile(data, fname):
    data.to_csv(fname, index=False)
    return

def main():
    city = "All-houses"
    k = 7
    num_neighbors = 10
    threshold_pct = 1
    feature_names = ['zestimate']
    # feature_names = ['sqft', 'zestimate']

    filename = "data/propertyInfo/{}.csv".format(city)
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate']
    data = read_csvfile(filename, header)
    data['cluster'] = -1

    '''
        Cluster houses using k-means Algorithm
    '''
    num_dim = len(feature_names)
    print("------- Clustering by {} --------".format(feature_names))
    feature_vectors = create_feature_vectors(data, feature_names)
    centroids = kmeans_mf(data, k, feature_vectors, num_dim, threshold_pct)


    '''
        Find similar houses using k-NN Algorithm
    '''
    # random_idx= random.randrange(0, len(data))
    random_idx = 8809
    new_house = data.iloc[random_idx]
    print("---- House Picked -----")
    print(new_house)

    print("------- Recommend {} houses --------".format(num_neighbors))
    normalized_feature_names = []
    for name in feature_names:
        normalized_feature_names.append(name + '_norm')
    recommended_houses = kNN(data, normalized_feature_names, num_dim, new_house, num_neighbors)
    print(recommended_houses)

    '''
        Write data to csv file
    '''
    write_fname = 'data/clustered_results/{}_{}f.csv'.format(city, num_dim)
    write_to_csvfile(data, write_fname)


if __name__ == '__main__':
    main()
