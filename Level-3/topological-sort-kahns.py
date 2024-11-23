#!/usr/bin/python

"""
Date: 2024-11-22

Description: Implementation of Kahn's algorithm to find a topological ordering.

Approach:
Kahn's algorithm finds a topological ordering by iteratively removing nodes in the graph which
have *no incoming edges*. When a node is removed from the graph, it is added to the topological
ordering and all its edges are removed allowing for the next set of nodes with no incoming edges
to be selected.

Applications: Used for dependent job scheduling like makefiles.

Reference:

Complexity: O(V + E)
"""

import collections

class Graph(object):
    """Implement methods to manage graph and find its topological order using kahn's algorithm."""

    def __init__(self):
        """Initialises a dictionary to store adjacency list of each vertex."""
        self.graph = collections.defaultdict(list)

    def addEdge(self, start, end):
        """Adds an edge to graph, updates adjacency list of source vertex."""
        self.graph[start].append(end)

    def getDistinctNodes(self):
        """Returns set of all distinct nodes present in graph."""
        nodes = set()
        for src in self.graph:
            nodes.add(src)
            for dest in self.graph.get(src, []):
                nodes.add(dest)
        return nodes

    def topologicalSort(self):
        """Finds topological ordering graph using kahn's algorithm."""
        indegree = {}
        for src in self.graph:
            for dest in self.graph.get(src, []):
                indegree[dest] = indegree.get(dest, 0) + 1
            
            # Add src also with 0 indegree so that indegree contain all the nodes in graph.
            if src not in indegree:
                indegree[src] = 0

        # Add nodes with 0 indegree to q.
        queue = collections.deque()
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        topSort = []
        while len(queue) != 0:
            node = queue.popleft()
            topSort.append(node)
            for neigh in self.graph.get(node, []):
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)

        # If topSort doesn't contain all nodes then graph has cycle.
        if len(topSort) != len(indegree):
            print('graph has cycle')
            return

        return topSort

g = Graph()
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print(g.topologicalSort()) # [5, 4, 2, 0, 3, 1]

g1 = Graph()
g1.addEdge(5, 2)
g1.addEdge(6, 2)

print(g1.topologicalSort()) # [5, 6, 2]
