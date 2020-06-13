# 选择排序不受输入数据的影响，即在任何情况下时间复杂度不变。
# 选择排序每次选出最小的元素，因此需要遍历 n-1 次。
# 平均时间复杂度：O(n^2),空间复杂度O(1)

import random
def selectSort(seq):
    # 遍历len(seq)-1轮
    for i in range(len(seq)-1):
        minIndex = i
        # 每轮遍历的元素
        for j in range(i+1,len(seq)-1):
            if seq[minIndex]>seq[j]:
                # 更新最小值的索引
                minIndex=j
                seq[i],seq[minIndex]=seq[minIndex],seq[i]
    return seq

seq = [9,8,7,6,5,4,3,2,1]
random.shuffle(seq)
print("排序前：{}".format(seq))
print("排序后：{}".format(selectSort(seq)))