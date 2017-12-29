#!/usr/bin/python

# Description:
# Programs checks if there exists a cycle in a graph or not.
#
# Complexity: 
# O(V + E)
# V = number of vertexes/nodes
# E = number of edges

from collections import defaultdict


class Graph(object):
  """Implements graph and performs DFS."""
  
  def __init__(self):
    """Initializes empty graph having no vertexes/edges."""
    
    self.graph = defaultdict(list)

  def add_edge(self, start, end):
    """Adds an edge to graph"""
    
    self.graph[start].append(end)

  def cycle_wrt_vertex(self, current_vertex, visited):
    """Uses DFS to check if cycle exists with respect to current vertex."""

    visited[current_vertex] = True

    for x in self.graph[current_vertex]:
      if visited.has_key(x):
        if visited[x] == False:
          return self.dfs_util(x, visited)
        else:
          return True

  def check_cycle(self):
    """Checks if cycle is present in a graph."""

    for k in self.graph.keys():
      visited = {k: False for k in self.graph.keys()}
      has_cycle = self.cycle_wrt_vertex(k, visited)
      if has_cycle:
        print "Graph has cycle !"
        print "Has a back edge with ancestor node - {0}".format(k)
        break

g = Graph()
g.add_edge(10, 11)
g.add_edge(10, 12)
g.add_edge(11, 13)
g.add_edge(13, 14)
g.add_edge(15, 15)

g.check_cycle()
