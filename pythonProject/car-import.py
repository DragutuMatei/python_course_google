import csv

input_file='cars.csv'
with open(input_file, 'r') as csv_file:
    rows = csv.reader(csv_file)
    header = rows.__next__()
    print(header)
    for row in rows:
        print(row)
