# 任务：
# 入队：在队列的一端插入元素 enqueue
# 出队：在队列的另一端删除元素 dequeue
# 判断队列是否为空 isEmpty
# 获取队列中元素个数 length

class ListQueue:
    def __init__(self):
        self.queue = []
        self.len = 0

    def enqueue(self,item):
        self.queue.append(item)
        self.len += 1

    def dequeue(self):
        if not self.isEmpty():
            self.queue.pop(0)
            self.len -= 1


    def isEmpty(self):
        if self.len == 0:
            return True
        else:
            return False

    def length(self):
        return self.len

q = ListQueue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.length())
q.dequeue()
print(q.length())
print(q.isEmpty())
