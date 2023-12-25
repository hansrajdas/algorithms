#!/usr/bin/python

# Date: 2021-03-30
#
# Description:
# Check if an undirected graph has cycle using union find(disjoint sets)
#
# Approach:
# Iterate over all edges of graph and keep on checking if any 2 vertice already
# belongs to same set, then there is a cycle otherwise do union of those 2
# vertices connected by an edge.
#
# References:
# https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/
#
# Complexity:
# Space: O(V + E)

class Disjoint:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        """
        Return parent (subset id) of element x. This can also be done *recursively*
        which is more intuitive and readable: Level-2/union_find.py.
        """
        # Find the root of the component/set
        root = x
        while root != self.parent[root]:
            root = self.parent[root]

        # Compress the path leading back to the root.
        # Doing this operation is called "path compression"
        # and is what gives us amortized time complexity.
        while x != root:
            _next = self.parent[x]
            self.parent[x] = root
            x = _next
        return root

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[xset] = yset
            self.rank[yset] += 1

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def has_cycle(self):
        disjoint_set = Disjoint(self.num_vertices)
        for u in self.graph:
            uset = disjoint_set.find(u)
            for v in self.graph[u]:
                vset = disjoint_set.find(v)
                if uset == vset:
                    return True
                disjoint_set.union(uset, vset)
        return False


def main():
    g = Graph(3)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(0, 2)

    assert g.has_cycle() == True

if __name__ == '__main__':
    main()
