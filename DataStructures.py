# Very basic, interview level implementations of fundamental data structures


##########################################################################
# LinkedList implementation, This list builds in front of head
##########################################################################
class ListNode(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)

class MyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def add_element(self, item):
        next_node = self.head
        self.head = ListNode(item)
        self.head.next = next_node

##########################################################################
# Tree Implementation (+ a regular graph)
##########################################################################
class TreeNode(object):
    def __init__(self, data=None):
            self.data = data
            self.children = []

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        n = TreeNode(node)
        self.children.append(n)


class MyTree(object):
    def __init__(self):
        self.head = TreeNode()


from collections import defaultdict
class MyGraph(object):
    def __init__(self):
        self.nodes = defaultdict(list)

    def add_edge(self, a, b):
        self.nodes[a].append(b)

    def dfs(self, node):
        visited = set()
        self._dfs(node,visited)

    def _dfs(self, node, visited):
        print(node)
        visited.add(node)

        for neighbor in self.nodes[node]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)

    def bfs(self, node):
        visited = set()
        queue = MyQueue()
        visited.add(node)
        queue.enqueue(node)

        while not queue.is_empty():
            n = queue.dequeue()
            print (n)
            for neighbor in self.nodes[n]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)





##########################################################################
# Binary Search Tree Implementation
##########################################################################
class BinaryTreeNode(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)

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
                self._insert(value, parent.left)
        else:
            if parent.right is None:
                parent.right = BinaryTreeNode(value)
            else:
                self._insert(value, parent.right)

    def in_order_traverse(self):
        self._in_order_traverse(self.root)

    def _in_order_traverse(self, node):
        if node is not None:
            self._in_order_traverse(node.left)
            print(node)
            self._in_order_traverse(node.right)


##########################################################################
# Stack implementation
##########################################################################
class MyStack(object):
    def __init__(self):
        self.l = MyLinkedList()
        self.size = 0

    def push(self, data):
        self.l.add_element(data)
        self.size += 1

    def pop (self):
        """
        In real implementation, needs to check if its empty and raise exception
        """
        item = self.l.head
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
# Not quite right now, should be a linked list anyway


# Linked list that builds after head
class MyForwardLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def add_element(self, item):
        if self.head is None:
            self.head = ListNode(item)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = ListNode(item)

class MyQueue(object):
    def __init__(self):
        self.size = 0
        self.l = MyForwardLinkedList()

    def enqueue(self, item):
        self.l.add_element(item)
        self.size += 1

    def dequeue(self):
        item = self.l.head
        self.l.head = self.l.head.next
        self.size -= 1
        return item.data

    def peek_front(self):
        return self.l.head.data

    def peek_back(self):
        cur = self.l.head
        while cur.next is not None:
            cur = cur.next
        return cur.next.data

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size==0

