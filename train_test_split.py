import csv
from sklearn.model_selection import train_test_split

r = []

with open('trainLabels_imbalanced.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        r.append(row)

train, val = train_test_split(r, test_size=0.1)

print(len(train))
print(len(val))

with open('train_imbalanced.csv', mode='w') as f:
    w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in train:
        w.writerow(row)

with open('val_imbalanced.csv', mode='w') as f:
    w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in val:
        w.writerow(row)