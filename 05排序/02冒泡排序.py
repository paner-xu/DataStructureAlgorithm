# 冒泡排序（顺序形式），从左向右，两两比较，
# 如果左边元素大于右边，就交换两个元素的位置。
# 其中，每一轮排序，序列中最大的元素浮动到最右面。
# 也就是说，每一轮排序，至少确保有一个元素在正确的位置。
# 当在一趟序列遍历中元素没有发生交换，则证明该序列已经有序。
# 平均时间复杂度：O(n^2),空间复杂度O(1)

import random
def bubleSort(seq):
    # 当一个列表的长度为len(seq)时，只需要经过len(seq)-1轮，排序就结束了
    for i in range(len(seq)-1):
        swap = False # 每一轮遍历都要重置swap
        # 这里面的i就是当前所在的轮数，j表示每一轮要遍历的元素
        for j in range(0,len(seq)-i-1):
            # 比较相邻两个元素的大小
            if seq[j]>seq[j+1]:
                swap = True
                seq[j],seq[j+1]=seq[j+1],seq[j]
        if not swap: # 当swap为False时，退出循环
            break
    return seq

seq = [9,8,7,6,5,4,3,2,1]
random.shuffle(seq)
print("排序前：{}".format(seq))
print("排序后：{}".format(bubleSort(seq)))