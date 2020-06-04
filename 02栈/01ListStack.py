# 任务:
# 压栈:在栈顶插入元素 push
# 弹栈：弹出栈顶元素 pop
# 获取栈顶元素 top
# 判断栈是否为空 isEmpty
# 获取栈中元素个数 length

class Stack():

    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
        # self.stack.insert(0,item)

    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()

    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def length(self):
        if len(self.stack) == 0:
            return 0
        else:
            return len(self.stack)

s = Stack()
s.push(12)
s.push(7)
s.push("Tony")
print(s.isEmpty())
print(s.length())
s.pop()
print(s.top())
s.pop()
print(s.length())
