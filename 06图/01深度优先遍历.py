class Node:
    # 定义一个结点类
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    # 创建二叉树，并添加结点
    def __init__(self):
        self.root = None

    # 添加元素
    def addNode(self, val):
        # 创建队列结构存储结点
        nodeStack = [self.root]

        # 如果根结点为空
        if self.root == None:
            self.root = Node(val)
            return

        while len(nodeStack) > 0:
            # 队列元素出列
            node = nodeStack.pop()
            # 如果左子结点为空
            if node.left == None:
                node.left = Node(val)
                return
            # 如果右子节点为空
            if node.right == None:
                node.right = Node(val)
                return
            nodeStack.insert(0, node.left)
            nodeStack.insert(0, node.right)

    # 深度优先
    def DFS(self, start_node):
        if start_node == None:
            return
        print(start_node.val)
        self.DFS(start_node.left)
        self.DFS(start_node.right)

bt = BinaryTree()
bt.addNode(0)
bt.addNode(1)
bt.addNode(2)
bt.addNode(3)
bt.addNode(4)
bt.addNode(5)
bt.addNode(6)
bt.addNode(7)
bt.addNode(8)
bt.addNode(9)

print("-----------深度遍历----------")
bt.DFS(bt.root)