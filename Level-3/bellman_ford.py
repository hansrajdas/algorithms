#!/usr/bin/python

# Date: 2018-01-28
#
# Description:
# Bellman ford can be used to find shortest path from a source to all reachable
# vertexes. Graph can have both positive and negative weights and cycles.
#
# Implementation:
# - Relax all edges |V| -1 times as there can be max of |V| -1 edges in any
#   simple path(from source any vertex in graph).
# - If there is a negative weight cycle then it reports and marks shortest
#   distance as undefined.
#
# Reference:
# https://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/
# 
# Complexity: O(VE)


class Graph(object):
  """Holds graph as adjacency list and implements methods to find shortest path
     Usig bellman ford algo."""

  def __init__(self):
    """Creates structure to hold distance to each vertex."""

    self.dist = {}
    self.edges = []

  def add_edge(self, src, dst, wgt):
    """Adds an edge to graph and initializes distance to added vertex in edge as
       infinity.

    Args:
      src: Source vertex.
      dst: Destination vertex.
      wgt: Weight of this vertex.
    """

    # As we are required to iterate over edges so it's better to keep edges as
    # list instead of coventionaly way of adjacency list.
    self.edges.append([src, dst, wgt])
    self.dist[src] = float("Inf")
    self.dist[dst] = float("Inf")

  def bellman_ford(self, source):
    """Finds shortest path or detects negative weight cycle in graph.
    
    Args:
      source: Source vertex from which shortest path is required.
    """

    number_of_vrtx = len(self.dist)
    self.dist[source] = 0 # Source is reachable with distance 0.

    for ctr in range(number_of_vrtx - 1):
      for u, v, w in self.edges:
        if self.dist[v] > self.dist[u] + w:
          self.dist[v] = self.dist[u] + w
    
    # If there is still scope of improvement, there is a negative weight cycle
    # in graph.
    # As the distance will keep on decreasing with each iteration of negative
    # edge cycle(will eventually become negative infinity if loop runs forever).
    cycle = False
    for u, v, w in self.edges:
      if self.dist[v] > self.dist[u] + w:
        cycle = True
    
    if cycle:
      print "There is negative wight cycle in graph so shortest path is undefined."
    else:
      for k in self.dist.keys(): 
        print "Vertex: {} \t Distance: {}".format(k, self.dist[k])

print "\n*********** Test case 1 ***********"
g = Graph()
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)
 
g.bellman_ford(0)

print "\n*********** Test case 2 ***********"
g1 = Graph()
g1.add_edge(0, 1, -1)
g1.add_edge(1, 0, -1)

g1.bellman_ford(0)
