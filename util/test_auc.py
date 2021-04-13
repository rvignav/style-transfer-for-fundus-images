from numpy import loadtxt
from sklearn.metrics import roc_auc_score

y_true = loadtxt('y_true_final_adam_balanced_notstylized.csv', delimiter=',')
targets = loadtxt('y_tot_final_adam_balanced_notstylized.csv', delimiter=',')

print(roc_auc_score(y_true, targets, multi_class='ovr'))