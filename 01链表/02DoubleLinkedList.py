# 1.创建节点类
# __init__()：初始化节点
# self.data：存储节点的值
# self.next：存储指向下一个节点的索引
# has_value()：将当前节点值和其他的值比较

class ListNode1:
    def __init__(self,data):
        # store data
        self.data = data
        # store index
        self.next = None
        self.previous = None
        return

    def has_value(self,value):
        if self.data == value:
            return True
        else:
            return False


# 2.创建单链表类管理节点
# __init__()：初始化对象
# list_length()：返回节点数量
# output_list():输出节点值
# add_list_item():在列表末尾增加一个新的节点
# unordered_search():根据一个特殊值去查询列表
# remove_list_item_by_id()：根据节点id移除节点

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        return

    # 添加节点
    def add_list_item(self, item):
        if isinstance(item, ListNode1):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item
            return

    def list_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def output_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return

    # 查询列表
    def unordered_search(self,value):
        current_node = self.head
        node_id = 1
        results = []
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
                current_node = current_node.next
                node_id += 1
        return results

    # 删除列表中的元素
    def remove_list_item_by_id(self,item_id):
        current_id = 1
        current_node = self.head
        previous_node = None
        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.previous = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None
                    return
            current_id += 1
            current_node = next_node

# 初始化节点对象
node1 = ListNode1(15)
node2 = ListNode1(8.2)
node3 = ListNode1('Berlin')
node4 = ListNode1(15)
track = DoubleLinkedList()
print("track length: %i" % track.list_length())
for current_node in [node1,node2,node3,node4]:
    track.add_list_item(current_node)
    print("track length: %i" % track.list_length())
    track.output_list()
results = track.unordered_search(15)
print(results)
track.remove_list_item_by_id(4)
track.output_list()


