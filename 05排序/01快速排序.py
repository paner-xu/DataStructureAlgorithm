# 对于一串序列，首先从中选取一个数，凡是小于这个数的值就被放在左边一摞，
# 凡是大于这个数的值就被放在右边一摞。然后，继续对左右两摞进行快速排序。
# 直到进行快速排序的序列长度小于 2 （即序列中只有一个值或者空值）
# 平均时间复杂度：O(nlogn),空间复杂度O(logn)

import random

def quickSort(seq):
    if len(seq)<=1:
        return seq
    base = seq[0]
    left = [seq[i] for i in range(1,len(seq)) if seq[i] < base]
    right = [seq[i] for i in range(1,len(seq)) if seq[i] >= base]
    # 通过递归，将左右两边的数进一步排序
    return quickSort(left) + [base] +quickSort(right)

seq = [9,8,7,6,5,4,3,2,1]
random.shuffle(seq)
print("排序前：{}".format(seq))
print("排序后：{}".format(quickSort(seq)))
