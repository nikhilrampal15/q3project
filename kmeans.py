import pandas as pd
import numpy as np

city = "san-francisco-ca"
filename = "data/propertyInfo/{}.csv".format(city)

header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate']
house = pd.read_csv(filename, sep='\t', names=header)
