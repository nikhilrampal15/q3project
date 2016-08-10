from glob import glob

with open('TX-houses.csv', 'a') as singleFile:
    for csv in glob('*-tx.csv'):
        if csv == 'TX-houses.csv':
            pass
        else:
            for line in open(csv, 'r'):
                singleFile.write(line)
