# 任务：
# 创建节点类
# 压栈:在栈顶插入元素 push
# 弹栈：弹出栈顶元素 pop
# 获取栈顶元素 top
# 判断栈是否为空 isEmpty
# 获取栈中元素个数 length

class LinkedStack():

    class Node:

        def __init__(self,item,next):
            self.item = item
            self.next = next

    def __init__(self):
        self.head = None
        self.len = 0

    def push(self,i):
        self.head = self.Node(i,self.head)
        self.len += 1

    def pop(self):
        if not self.isEmpty():
            item = self.head.item
            self.head = self.head.next
            self.len -= 1

    def top(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.head.item

    def length(self):
        return self.len

    def isEmpty(self):
        if self.len == 0:
            return True
        else:
            return False

s = LinkedStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.length())
s.pop()
print(s.length())
s.push(12)
print(s.top())



