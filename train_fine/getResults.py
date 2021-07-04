import os


def getMAE():
    f_gt = open('test_labels.csv', 'r')
    gt_lines = f_gt.readlines()
    f_gt.close()

    f_pre = open('ckpts/IA2NIMA/AVA/output.txt','r')
    pre_lines = f_pre.readlines()
    pre_lines = pre_lines[1:]
    f_pre.close()

    print(gt_lines[0],'++')
    print(pre_lines[0],'--')


getMAE()