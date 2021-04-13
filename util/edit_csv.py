import csv
from random import sample

no = []
dr = []

with open('trainLabels.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        if (row[1] == '0'):
            no.append(row)
        else:
            dr.append(row)

no = sample(no, int(0.2 * len(no)))

print(len(no))
print(len(dr))

with open('trainLabels_balanced.csv', mode='w') as f:
    w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in no:
        w.writerow(row)
    for row in dr:
        w.writerow(row)

