#!/usr/bin/python

# Date: 2017-12-28
#
# Description:
# Depth first search of a directed graph.
#
# Approach:
# Dictionary is used to store graph # information as adjacency list. Uses
# dictionary to store adjacency list of graph having list of adjacent nodes
# corresponding to each node.
#
# Recursion is used to visit all reachable nodes with respect to start node.
# Use a visited dictionary to keep track all nodes that are already visited.
#
# Complexity:
# O(V + E)
# V = number of vertexes/nodes
# E = number of edges

import collections


class Graph(object):
  """Implements graph and performs DFS."""

  def __init__(self):
    """Initializes empty graph having no vertexes/edges."""
    self.graph = collections.defaultdict(list)

  def add_edge(self, start, end):
    """Adds an edge to graph"""
    self.graph[start].append(end)

  def dfs_util(self, current_vertex, visited):
    """Utility function for DFS from some current vertex"""
    print current_vertex
    visited[current_vertex] = True

    for x in self.graph[current_vertex]:
      if visited.has_key(x):
        if not visited[x]:
          self.dfs_util(x, visited)
        else:
          pass
      else:
          print '{0} - dont have any adjacent vertex'.format(x)

  def dfs_specific(self, start):
    """
    Perfoms DFS traversal from a specific vertex - start .i.e will traverse
    all vertexes reachable from start
    """
    print '\nTraversing vertexes reachable from {0}'.format(start)
    visited = {v : False for v in self.graph}
    self.dfs_util(start, visited)

  def dfs_all(self):
    """Perfoms DFS traversal such that all vertexes in a graph gets covered."""

    print '\nTraversing all vertexes'
    visited = {k: False for k in self.graph}

    for k in self.graph:
      if not visited[k]:
        self.dfs_util(k, visited)
      else:
        pass

g = Graph()
g.add_edge(10, 11)
g.add_edge(10, 12)
g.add_edge(11, 13)
g.add_edge(13, 14)
g.add_edge(15, 16)

# This gives 10, 11, 13, 14, 12.
# Note that 15, 16 is not reachable from 10 so these 2 vertexes will not be
# printed.
g.dfs_specific(10)

# To traverse all vertexes of a graph we will use modified dfs.
g.dfs_all()


# Output:
# -----------------------
# Traversing vertexes reachable from 10
# 10
# 11
# 13
# 14 - dont have any adjacent vertex
# 12 - dont have any adjacent vertex
#
# Traversing all vertexes
# 10
# 11
# 13
# 14 - dont have any adjacent vertex
# 12 - dont have any adjacent vertex
# 15
# 16 - dont have any adjacent vertex
