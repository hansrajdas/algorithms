#!/usr/bin/python

# Date: 2017-12-29
#
# Description:
# Program to check if there exists a cycle in a graph or not.
#
# Approach:
# - Graph has cycle if it contains a back edge(there is some other path which
#   reaches to the same vertex from a source vertex).
# - This uses DFS approach to find back edge.
# - This is implemented for directed graph, for undirected graph we just have to
#   edge corresponding to each edge(for each edge u to v there should be an
#   edge from v to u)
#
# Reference:
# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
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

  def cycle_wrt_vertex(self, current_vertex, visited):
    """Uses DFS to check if cycle exists with respect to current vertex."""
    visited[current_vertex] = True

    for x in self.graph[current_vertex]:
      if visited.has_key(x):
        if not visited[x]:
          return self.cycle_wrt_vertex(x, visited)
        else:
          return True

  def check_cycle(self):
    """Checks if cycle is present in a graph."""
    for k in self.graph:
      visited = {k: False for k in self.graph}
      has_cycle = self.cycle_wrt_vertex(k, visited)
      if has_cycle:
        print 'Graph has cycle!'
        print 'Has a back edge with ancestor node - {0}'.format(k)
        break


g = Graph()
g.add_edge(10, 11)
g.add_edge(10, 12)
g.add_edge(11, 13)
g.add_edge(13, 14)
g.add_edge(15, 15)

g.check_cycle()
