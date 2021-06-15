from numpy import loadtxt
from sklearn.metrics import roc_auc_score
import csv
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--stylized', help='y/n')
args = parser.parse_args()
s = args.stylized == 'y'

labels = {}

y_true = []

with open('y_true.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = -1
    for row in csv_reader:
        line_count += 1
        if line_count == 0:
            continue
        val = int(row[1])
        if val != 0:
            val = 1
        labels[row[0]] = val

if s:
    fname = 'submission_S->S.csv'
else:
    fname = 'submission_NS->NS.csv'

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = -1
    for row in csv_reader:
        line_count += 1
        if line_count == 0:
            continue
        ID = row[0]
        y_true.append(labels[ID])

if s:
    targets = loadtxt('preds_S->S.txt', delimiter=' ')[:, 1]
else:
    targets = loadtxt('preds_NS->NS.txt', delimiter=' ')[:, 1]

if s:
    sub = 'S->S: '
else:
    sub = 'NS->NS: '

print(sub + str(roc_auc_score(y_true, targets)))