# 任务：
# 创建节点类
# 入队：在队列的一端插入元素 enqueue
# 出队：在队列的另一端删除元素 dequeue
# 判断队列是否为空 isEmpty
# 获取队列中元素个数 length

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.len = 0

    def enqueue(self,i):
        elem = Node(i,None)
        if self.isEmpty():
            self.front = elem
            self.rear = elem
        else:
            self.rear.next = Node(i,None)
        self.len += 1

    def dequeue(self):
        if not self.isEmpty():
            self.front = self.front.next
            self.len -= 1

    def isEmpty(self):
        if self.len == 0:
            return True
        if self.len != 0:
            return  False

    def length(self):
        return self.len

q = LinkedQueue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.length())
q.dequeue()
print(q.length())
print(q.isEmpty())