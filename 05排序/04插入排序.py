# 对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
# 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
# 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
# 平均时间复杂度：O(n^2),空间复杂度O(1)

import random

def insertSort(seq):
    for i in range(len(seq)-1):
        # 保存当前待插入的元素
        curNum,preIndex = seq[i+1],i
        # 比较当前的数与前一个数的大小
        while preIndex >= 0 and curNum < seq[preIndex]:
            # 跟新待插入的数的位置
            seq[preIndex+1]=seq[preIndex]
            preIndex -= 1
        seq[preIndex+1]=curNum
    return seq

seq = [9,8,7,6,5,4,3,2,1]
random.shuffle(seq)
print("排序前：{}".format(seq))
print("排序后：{}".format(insertSort(seq)))