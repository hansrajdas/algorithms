#!/usr/bin/python

# Date: 2017-12-29
#
# Description:
# Program to check if there exists a cycle in a directed graph or not.
#
# Approach:
# - Graph has cycle if it contains a back edge(there is some other path which
#   reaches to the same vertex from a source vertex).
# - This uses DFS approach to find back edge.
# - This is implemented for directed graph, for undirected graph we just have
#   to add an edge corresponding to each edge(for each edge u to v there should
#   be an edge from v to u)
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
    if current_vertex in visited:
        return True
    visited.add(current_vertex)
    for x in self.graph.get(current_vertex, []):
        if self.cycle_wrt_vertex(x, visited):
            return True
    visited.remove(current_vertex)
    return False

  def check_cycle(self):
    """Checks if cycle is present in a graph."""
    for k in self.graph:
      # This can't be done using set as we have to check for back edge and node
      # which has an outgoing edge can only have back edge so to keep track of
      # nodes having outgoing edges, we has to use dict with True/False values
      visited = set()
      if self.cycle_wrt_vertex(k, visited):
        print('Graph has cycle!')
        print('Has a back edge with ancestor node - {0}'.format(k))
        break


# Case: 1
g = Graph()
g.add_edge(10, 11)
g.add_edge(10, 12)
g.add_edge(11, 13)
g.add_edge(13, 14)
g.add_edge(15, 15)  # Create cycle

g.check_cycle()

# Case: 2
g = Graph()

g.add_edge('a', 'd')
g.add_edge('f', 'b')
g.add_edge('b', 'd')
g.add_edge('f', 'a')
g.add_edge('d', 'c')
g.add_edge('d', 'a')  # Create cycle

g.check_cycle()
