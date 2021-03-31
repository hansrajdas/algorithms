#!/usr/bin/python

# Date: 2021-03-31
#
# Description:
# Given an undirected weighted graph, find minimum spanning tree.
#
# Approach:
# Spanning tree of a graph is set of edges which covers all nodes but don't 
# form a cycle. Mininum spanning tree(MST) is one which has min weight(sum of
# weight of edges included).
#
# Approach is to sort all edges by weight in non decreasing order then pick
# each edge and check if it forms a cycle? If it does not form a cycle include
# that edge otherwise discard that and move ahead.
# To check if edge form a cycle or not, we can use union find data structure.
#
# MST should have V - 1 number of edges in it, V = number of vertices in graph
#
# Reference:
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
#
# Complexity:
# O(ElogE)

class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return

        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        else:
            self.parent[xset] = yset
            self.rank[yset] += 1

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def kruskalsMST(self):
        union_find = Disjoint(self.V)

        mst = []
        self.graph = sorted(self.graph, key=lambda x: x[2])

        edges = 0
        i = 0
        while edges < self.V - 1:
            u, v, w = self.graph[i]
            uset = union_find.find(u)
            vset = union_find.find(v)

            if uset != vset:
                union_find.union(u, v)
                mst.append((u, v, w))
                edges += 1
            i += 1

        # Print MST
        mst_cost = 0
        for u, v, w in mst:
            mst_cost += w
            print('%d -- %d == %d' % (u, v, w))
        print('Minimum Spanning Tree' , mst_cost)

def main():
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
     
    g.kruskalsMST()
    # 2 -- 3 == 4
    # 0 -- 3 == 5
    # 0 -- 1 == 10
    # Minimum Spanning Tree 19

main()
