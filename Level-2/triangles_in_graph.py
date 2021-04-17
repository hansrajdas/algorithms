#!/usr/bin/python

# Date: 2021-04-13
#
# Description:
# Given a Graph, count number of triangles in it. The graph can be directed
# or undirected.
#
# Approach:
# The idea is to use three nested loops to consider every triplet (i, j, k)
# and check for the above condition (there is an edge from i to j, j to k and
# k to i) 
#
# However in an undirected graph, the triplet (i, j, k) can be permuted to give
# six combination (See previous post for details). Hence we divide the total
# count by 6 to get the actual number of triangles. 
#
# In case of directed graph, the number of permutation would be 3 (as order of
# nodes becomes relevant). Hence in this case the total number of triangles
# will be obtained by dividing total count by 3. For example consider the
# directed graph given below 
#
# Reference:
# https://www.geeksforgeeks.org/number-of-triangles-in-directed-and-undirected-graphs/
# https://www.geeksforgeeks.org/number-of-triangles-in-a-undirected-graph/
#
# Complexity:
# O(V^3)


def get_triangles_in_graph(g, is_directed):
    ans = 0
    n = len(g)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and k != i and g[i][j] and g[j][k] and g[k][i]:
                    ans += 1

    return ans // 3 if is_directed else ans // 6

# Create adjacency matrix of an undirected graph
graph = [[0, 1, 1, 0],
         [1, 0, 1, 1],
         [1, 1, 0, 1],
         [0, 1, 1, 0]]
# Create adjacency matrix of a directed graph
digraph = [[0, 0, 1, 0],
           [1, 0, 0, 1],
           [0, 1, 0, 0],
           [0, 0, 1, 0]]

print("The Number of triangles in undirected graph : %d" %
      get_triangles_in_graph(graph, False))

print("The Number of triangles in directed graph : %d" %
      get_triangles_in_graph(digraph, True))
