#!/usr/bin/python

# Date: 2018-01-26
#
# Description:
# This solution is for directed acyclic graph(DAG) only, that is this
# implementation does not allow cycles in graph but graph can have negative
# edges also as opposed by dijkstra.
# 
# Idea is to first sort graph in topological order with respect to source vertex
# and then update the weights based on previous weights. If current weight(from
# source) for a vertex v is more than a vertex weight(s, u) + weight(u, v) then
# update weight(from source) of v as weight(s, u) + weight(u, v).
#
# Reference:
# https://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/
#
# Complexity: O(V + E).


from collections import defaultdict


class Graph(object):
  """Implements graph and functions for shortest path."""

  def __init__(self):
    """Initializes data structure to store in adjacency list and distance."""

    self.graph = defaultdict(list)
    self.dist = {}

  def add_edge(self, u, v, w):
    """Adds an edge to graph and initialzes distance to vertexes added as
       infinity.
    
    Args:
      u: Source vertex in edge.
      v: Destination vertex in edge.
      w: Weight of edge to be added.
    """ 

    self.graph[u].append((v, w))
    self.dist[u] = float("Inf")
    self.dist[v] = float("Inf")

  def toplogical_sort(self, source, visited, stack):
    """Updates stack with topological order w.r.t source vertex.

    Args:
      source: Starting vertex.
      visited: Dictionary to store visited status.
      stack: Stack to hold topological order.
    """

    visited[source] = True
    for adjacent in self.graph[source]:
      if self.graph.has_key(adjacent[0]) and (not visited[adjacent[0]]):
        self.toplogical_sort(adjacent[0], visited, stack)
      else:
        if adjacent[0] not in stack:
          stack.append(adjacent[0])
    stack.append(source)

  def shortest_path(self, s):
    """Prints shortest path w.r.t given source vertex.
    
    Args:
      s: Source vertex from which shortest path is required.
    """

    stack = [] # To store topological order.

    if self.graph.has_key(s):
      # Find topological order.
      visited = {v: False for v in self.graph.keys()}
      self.toplogical_sort(s, visited, stack)
    else:
      print "None of the vertex is reachable from {}, so  no shortest path".format(s)

    stack.reverse() # Get correct topological order.

    # Source node is at 0 distance/weight.
    self.dist[s] = 0
    for u in stack:
      for v, w in self.graph[u]:
        if self.dist[v] > self.dist[u] + w:
          self.dist[v] = self.dist[u] + w

    print "\nVertex and distance"
    for n in self.dist:
      print "Vertex: {} Distance: {}".format(n, self.dist[n])

g = Graph()
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 4)
g.add_edge(2, 3, 4)
g.add_edge(4, 3, 4)
g.add_edge(5, 3, 4)
g.shortest_path(1)
del g
g = Graph()
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 6)
g.add_edge(1, 2, 2)
g.add_edge(2, 4, 4)
g.add_edge(2, 5, 2)
g.add_edge(2, 3, 7)
g.add_edge(3, 4, -1)
g.add_edge(4, 5, -2)
g.shortest_path(1)

# Output:
# Vertex and distance
# Vertex: 1 Distance: 0
# Vertex: 2 Distance: 3
# Vertex: 3 Distance: 4
# Vertex: 4 Distance: inf
# Vertex: 5 Distance: inf
# 
# Vertex and distance
# Vertex: 0 Distance: inf
# Vertex: 1 Distance: 0
# Vertex: 2 Distance: 2
# Vertex: 3 Distance: 6
# Vertex: 4 Distance: 5
# Vertex: 5 Distance: 3
