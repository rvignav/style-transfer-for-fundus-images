from numpy import loadtxt
from sklearn.metrics import roc_auc_score
import csv
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--stylized', help='a (S->S)/b (NS->NS)/c (S->NS)')
args = parser.parse_args()
s = args.stylized

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

if s == 'a':
    fname = 'submission_S->S.csv'
elif s == 'b':
    fname = 'submission_NS->NS.csv'
else:
    fname = 'submission_S->NS.csv'

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = -1
    for row in csv_reader:
        line_count += 1
        if line_count == 0:
            continue
        ID = row[0]
        y_true.append(labels[ID])

if s == 'a':
    targets = loadtxt('preds_S->S.txt', delimiter=' ')[:, 1]
elif s == 'b':
    targets = loadtxt('preds_NS->NS.txt', delimiter=' ')[:, 1]
else:
    targets = loadtxt('preds_S->NS.txt', delimiter=' ')[:, 1]

if s == 'a':
    sub = 'S->S: '
elif s == 'b':
    sub = 'NS->NS: '
else:
    sub = 'S->NS: '

print(sub + str(roc_auc_score(y_true, targets)))