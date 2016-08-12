import pandas as pd
import numpy as np

def parse_int(data):
    data_int = []
    for item in data:
        if item == "Studio" or item == "--":
            data_int.append(0)
        else:
            data_int.append(int(item))
    return data_int

def parse_float(data):
    data_float = []
    for item in data:
        if item == "--":
            data_float.append(0)
        else:
            data_float.append(float(item))
    return data_float

def parse_zestimate(data):
    data_int = []
    mean_zestimate = cal_zestimate_mean(data)
    for item in data:
        if item == "Unavailable":
            data_int.append(mean_zestimate)
        else:
            data_int.append(int(item))
    return data_int

def cal_zestimate_mean(data):
    total = 0
    count = 0
    for item in data:
        if item != 'Unavailable':
            total += int(item)
            count += 1
    return total / count

def read_csvfile(filename, header):
    data = pd.read_csv(filename, sep=',', skiprows=[0], names=header)
    data['bedroom'] = parse_int(data['bedroom'])
    data['bathroom'] = parse_float(data['bathroom'])
    data['sqft'] = parse_int(data['sqft'])
    data['zestimate'] = parse_zestimate(data['zestimate'])
    return data

def main():
    city = "san-jose-ca"
    header = ['zpid','street', 'city', 'state', 'zipcode', 'bedroom', 'bathroom', 'sqft', 'zestimate']
    data = read_csvfile("data/propertyInfo/{}.csv".format(city), header)
    print(data)

if __name__ == '__main__':
    main()
