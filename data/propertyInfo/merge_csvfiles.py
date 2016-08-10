from glob import glob

with open('All-houses.csv', 'a') as singleFile:
    for csv in glob('*.csv'):
        if csv == 'All-houses.csv':
            pass
        else:
            for line in open(csv, 'r'):
                singleFile.write(line)
