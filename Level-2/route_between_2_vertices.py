#!/usr/bin/python

# Date: 2020-10-20
#
# Description:
# Given a directed graph, design an algorithm to find out whether there is a
# route between 2 nodes.
#
# Approach:
# Starting from source node, use breadth first(BFS) approach to find if we are
# able to find to destination node or not.
#
# Complexity:
# O(V + E) Time
# O(V) Space

import collections

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dst):
        if src in self.graph:
            self.graph[src].append(dst)
        else:
            self.graph[src] = [dst]

    def has_path(self, src, dst):
        """Checks if there is a path from source to destination vertex."""
        if src == dst:
            return True

        Q = collections.deque([src])
        visited = set()
        while Q:
            curr = Q.popleft()
            visited.add(curr)
            for adj in self.graph.get(curr, []):
                if adj == dst:
                    return True
                if adj not in visited:
                    Q.append(adj)
        return False

def main():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(2, 1)

    assert g.has_path(1, 2) == True
    assert g.has_path(1, 4) == True
    assert g.has_path(4, 1) == False


if __name__ == '__main__':
    main()
