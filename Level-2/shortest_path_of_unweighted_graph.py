#!/usr/bin/python

# Date: 2020-12-29
#
# Description:
# Find shortest path from a source to destination in a unweighted graph
#
# Approach:
# For unweighted graph, we can use BFS traversal to find shortest path
# - BFS traverses graph layer by layer so when we reach a node it must be
#   reached with shortest path in an unweighted graph
# - We can slightly modify BFS and keep on saving node which helped in reaching
#   a particulatr node which then can be used to reconstruct path or len of path
#
# Complexity:
# O(V + E)

import collections

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dst):
        if src in self.graph:
            self.graph[src].append(dst)
        else:
            self.graph[src] = [dst]

    def bfs(self, src):
        """
        Traverses graph using BFS and returns `prev` dict which gives parent
        of a node.
        """
        prev = {}  # Save which node helped us reaching a given node - parent of given node
        Q = collections.deque([src])
        visited = set()
        while Q:
            node = Q.popleft()
            visited.add(node)
            for next_node in self.graph.get(node, []):
                if next_node not in visited:
                    Q.append(next_node)
                    prev[next_node] = node  # Save parent of next_node as node
        return prev

    def reconstruct_path(self, src, dst, prev):
        """Constructs path from src to dst node using prev dictionary."""
        path = [dst]
        parent = prev.get(dst)
        while parent:
            path.append(parent)
            parent = prev.get(parent)
        path.reverse()

        if path[0] == src:
            return path
        return []  # Path from src to dst doesn't exists

    def shortest_path(self, src, dst):
        """Finds shortest path from source to dst in an unweighted graph."""
        prev = self.bfs(src)
        path = self.reconstruct_path(src, dst, prev)
        print(f'Shortest path from {src} to {dst}: {path}')

def main():
    g = Graph()
    g.add_edge(10, 11)
    g.add_edge(10, 12)
    g.add_edge(11, 13)
    g.add_edge(13, 14)
    g.add_edge(15, 16)

    g.shortest_path(10, 14)
    g.shortest_path(10, 12)
    g.shortest_path(11, 14)
    g.shortest_path(15, 16)
    g.shortest_path(13, 16)

if __name__ == '__main__':
    main()


# Output:
# -------
# Shortest path from 10 to 14: 10->11->13->14
# Shortest path from 10 to 12: 10->12
# Shortest path from 11 to 14: 11->13->14
# Shortest path from 15 to 16: 15->16
# Shortest path from 13 to 16: not found
