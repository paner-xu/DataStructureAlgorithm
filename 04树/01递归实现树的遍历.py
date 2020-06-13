# 任务：
# 定义节点类
# 定义树类
# 为树添加节点 addNode
# 递归实现先序遍历 frontRecursion
# 递归实现中序遍历 midRecursion
# 递归实现后序遍历 laterRecursion

# 先序遍历思想：先访问根节点，再先序遍历左子树，然后再先序遍历右子树。总的来说是根—左—右
# 中序思想：先中序访问左子树，然后访问根，最后中序访问右子树。总的来说是左—根—右
# 后序思想：先后序访问左子树，然后后序访问右子树，最后访问根。总的来说是左—右—根


class Node:
    def __init__(self,elem=-1,l_child=None,r_child=None):
        self.elem = elem
        self.l_child = l_child
        self.r_child = r_child

class Tree:
    def __init__(self):
        self.root = Node()
        self.queue = []

    def addNode(self,elem):
        node = Node(elem)
        # 判断根节点是否为空，如果为空，则赋值给根节点
        if self.root.elem == -1:
            self.root = node
            self.queue.append(node)
        # 如果不为空，则赋值给儿子节点
        else:
            treeNode = self.queue[0]
            if treeNode.l_child is None:
                treeNode.l_child = node
                self.queue.append(treeNode.l_child)
            else:
                treeNode.r_child = node
                self.queue.append(treeNode.r_child)
                self.queue.pop(0)

    def frontRecursion(self,root):
        if root is not None:
            print(root.elem)
            self.frontRecursion(root.l_child)
            self.frontRecursion(root.r_child)

    def midRecursion(self,root):
        if root is not None:
            self.midRecursion(root.l_child)
            print(root.elem)
            self.midRecursion(root.r_child)

    def laterRecursion(self,root):
        if root is not None:
            self.laterRecursion(root.l_child)
            self.laterRecursion(root.r_child)
            print(root.elem)

tree = Tree()
for elem in range(10):
    tree.addNode(elem)
print("---------------先序遍历-------------------")
print(tree.frontRecursion(tree.root))
print("---------------中序遍历-------------------")
print(tree.midRecursion(tree.root))
print("---------------后序遍历-------------------")
print(tree.laterRecursion(tree.root))
