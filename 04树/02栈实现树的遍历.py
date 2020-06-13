# 任务：
# 定义节点类
# 定义树类
# 为树添加节点 addNode
# 递归实现先序遍历 frontStack
# 递归实现中序遍历 midStack
# 递归实现后序遍历 laterStack

# 先序遍历思想：先访问根节点，再先序遍历左子树，然后再先序遍历右子树。总的来说是根—左—右
# 中序思想：先中序访问左子树，然后访问根，最后中序访问右子树。总的来说是左—根—右
# 后序思想：先后序访问左子树，然后后序访问右子树，最后访问根。总的来说是左—右—根

class Node(object):
    """节点类"""

    def __init__(self, elem=-1, l_child=None, r_child=None):
        self.elem = elem
        self.l_child = l_child
        self.r_child = r_child


class Tree(object):
    """树类"""

    def __init__(self):
        self.root = Node()
        self.queue = []

    def add_node(self, elem):
        """为树添加节点"""

        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root.elem == -1:
            self.root = node
            self.queue.append(self.root)
        else:
            treeNode = self.queue[0]
            # 此结点没有左子树，则创建左子树节点
            if treeNode.l_child is None:
                treeNode.l_child = node
                self.queue.append(treeNode.l_child)
            else:
                treeNode.r_child = node
                self.queue.append(treeNode.r_child)
                # 如果该结点存在右子树，将此节点丢弃
                self.queue.pop(0)

    @staticmethod
    def frontStack(root):
        if root:
            stack = []
            node = root
            while node or stack:
                # 从根节点开始，一直找它的左子树
                while node:
                    print(node.elem)
                    stack.append(node)
                    node = node.l_child
                # while结束表示当前节点node为空，即前一个节点没有左子树了
                node = stack.pop()
                # 开始查看它的右子树
                node = node.r_child

    @staticmethod
    def midStack(root):
        if root:
            stack = []
            node = root
            while node or stack:
                # 从根节点开始，一直找它的左子树
                while node:
                    stack.append(node)
                    node = node.l_child
                # while结束表示当前节点node为空，即前一个节点没有左子树了
                node = stack.pop()
                print(node.elem)
                # 查看右子树
                node = node.r_child

    @staticmethod
    def laterStack(root):
        if root:
            stack1 = []
            stack2 = []
            node = root
            stack1.append(node)
            # 找出后序遍历的逆序，存在stack2里面
            while stack1:
                node = stack1.pop()
                if node.l_child:
                    stack1.append(node.l_child)
                if node.r_child:
                    stack1.append(node.r_child)
                stack2.append(node)
            # 将stack2中的元素出栈，即为后序遍历次序
            while stack2:
                print(stack2.pop().elem)

# 生成十个数据作为树节点
elements = range(10)
tree = Tree()
for elem in elements:
    tree.add_node(elem)
print("---------------先序遍历-------------------")
# print(tree.frontStack(tree.root))
tree.frontStack(tree.root)
print("---------------中序遍历-------------------")
# print(tree.midStack(tree.root))
tree.midStack(tree.root)
print("---------------后序遍历-------------------")
# print(tree.laterStack(tree.root))
tree.laterStack(tree.root)