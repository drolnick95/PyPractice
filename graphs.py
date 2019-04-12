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

# You are given a list of projects and a list of dependencies(which is a list of pairs of projects,
# where the second project is dependent on the first project) Find a build ordere that will allow the projects
# to be bulit
# EX: input:
# projects: ['a','b','c','d','e','f']
# dependencies:[('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]
# OUTPUT: ['e', 'f', 'a', 'b', 'd', 'c']


def build_order (projs,deps):
    counts = {}
    for proj in projs:
        counts[proj] = [0]
    order = []
    for tup in deps:
        counts[tup[1]][0]+=1
        counts[tup[0]].append(tup[1])

    while counts:
        for p in list(counts.keys()):
            if counts[p][0] == 0:
                order.append(p)
                for neighbor in counts[p][1:]:
                    counts[neighbor][0]-=1
                del(counts[p])
    return order








