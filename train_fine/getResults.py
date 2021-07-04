import os
import numpy as np
from sklearn.metrics import mean_absolute_error

def getMAE():
    f_gt = open('test_labels.csv', 'r')
    gt_lines = f_gt.readlines()
    f_gt.close()

    f_pre = open('ckpts/IA2NIMA/AVA/output.txt','r')
    pre_lines = f_pre.readlines()
    pre_lines = pre_lines[1:]
    f_pre.close()

    dict_gt = {}
    for line in gt_lines:
        ll = line.split(',')
        dict_gt[ll[0]] = [float(x) for x in ll[1:]]

    y_true = []
    y_pre = []
    for line in pre_lines:
        ll = line.split('.jpg,"[')
        gt = dict_gt[ll[0]]
        y_true.append(gt)
        pre = list(ll[1].split(']')[0].split(','))
        pre = [float(x) for x in pre]
        y_pre.append(pre)
    return mean_absolute_error(y_true, y_pre)

MAE = getMAE()
print('MAE::', MAE)