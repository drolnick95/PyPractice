# Very basic, interview level implementations of fundamental data structures


##########################################################################
# LinkedList implementation
##########################################################################
class ListNode(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class MyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def add_element(self, item):
        next_node = self.head
        self.head = ListNode(item)
        self.head.next = next_node

##########################################################################
# Tree Implementation
##########################################################################
class TreeNode(object):
    def __init__(self, data=None):
            self.data = data
            self.children = []

    def insert(self, node):

            self.children.append(node)


class MyTree(object):
    def __init__(self,head):
        self.head = head


##########################################################################
# Binary Tree Implementation #
##########################################################################
class BinaryTreeNode(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class MyBinaryTree(object):
    def __init__(self,root):
        self.root = BinaryTreeNode(root)

    def insert(self, value):
        self._insert(value, self.root)

    def _insert(self, value, parent):
        if value < parent.data:
            if parent.left is None:
                parent.left = BinaryTreeNode(value)
            else:
                parent._insert(value, parent.left)
        else:
            if parent.right is None:
                parent.right = BinaryTreeNode(value)
            else:
                self._insert(value, parent.right)


##########################################################################
# Stack implementation
##########################################################################
class myStack(object):
    def __init__(self):
        self.l = MyLinkedList()
        self.size = 0

    def push(self, data):
        self.l.add_element(data)
        self.size += 1

    def pop (self):
        item = self.l
        self.l.head = self.l.head.next
        self.size -= 1
        return item

    def peek(self):
        return self.l.head

    def size(self):
        return self.size


##########################################################################
# Queue implementation using python array
##########################################################################
class MyQueueArr(object):
    def __init__(self):
        self.size = 0
        self.arr = []

    def enqueue(self, item):
        self.arr.append(item)
        self.size += 1

    def dequeue(self):
        item = self.arr[self.size-1]
        self.arr[self.size-1] = None
        self.size -=1
        return item

    def peek_front(self):
        return self.arr[0]

    def peek_back(self):
        return self.arr[self.size-1]

    def size(self):
        return self.size


