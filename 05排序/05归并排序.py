# 1.申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
# 2.设定两个指针，最初位置分别为两个已经排序序列的起始位置；
# 3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
# 4.重复步骤 3 直到某一指针达到序列尾；
# 5.将另一序列剩下的所有元素直接复制到合并序列尾。
# 平均时间复杂度：O(nlogn),空间复杂度O(n)

import random

def mergeSort(seq):
    if len(seq)<=1:
        return seq
    mid = len(seq)//2
    left = seq[:mid]
    right = seq[mid:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left,right):
    result = [] # 储存最后的结果
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result = result + left[i:] + right[j:] # 剩余元素直接添加到末尾
    return result

seq = [9,8,7,6,5,4,3,2,1]
random.shuffle(seq)
print("排序前：{}".format(seq))
print("排序后：{}".format(mergeSort(seq)))
