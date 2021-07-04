import os


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

    all = 0.
    num = 0
    for line in pre_lines:
        ll = line.split('.jpg,')
        print(ll,'+++===')
        gt = dict_gt[ll[0]]
        pre = list(ll[1])
        pre = [float(x) for x in pre]
        print(gt,'++')
        print(pre,'--')

getMAE()