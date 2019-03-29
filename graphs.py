# Given a directed graph, design an algorithm to find out whether there is a route between two nodes
# DFS implementation, could also be done with BFS
def is_route(graph, start, target):
    visited = set()
    return _is_route(start, target, visited, graph)


def _is_route(start, target, visited, graph):
    if start == target:
        return True
    visited.add(start)
    for neighbor in graph.nodes[start]:
        if neighbor not in visited:
            return _is_route(neighbor, target, visited, graph)
        return False

# Given a sorted array with unique integer elemets, write an algorithm to create a bst with minimal height

class TreeNode(object):
    def __init__(self, data):
        self.data=data
        self.left = None
        self.right = None

class MinBST(object):
    def __init__(self):
        self.head = None

    def build_minimal_tree(self,arr):
        self.head = self._build_minimal_tree(arr, 0, len(arr)-1)

    def _build_minimal_tree(self,arr,first, last):
        if first>last:
            return None

        mid = int((last+first)/2)
        node = TreeNode(arr[mid])
        node.left = self._build_minimal_tree(arr, first, mid-1)
        node.right = self._build_minimal_tree(arr, mid+1, last)
        return node












