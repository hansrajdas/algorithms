#!/usr/bin/python

"""
Date: 2018-01-28

Description:
Bellman ford can be used to find shortest path from a source to all reachable
vertexes. Graph can have both positive and negative weights and cycles.

Implementation:
- Relax all edges |V| - 1 times as there can be max of |V| - 1 edges in any
  simple path(from source any vertex in graph).
- Run above step second time and if there is a negative weight cycle(if we
  still see more optimal shortest path) then it reports and marks shortest
  distance as undefined.

Reference:
https://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/

Complexity:
O(VE)
"""


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
    # list instead of coventional way of adjacency list.
    self.edges.append([src, dst, wgt])
    self.dist[src] = float('Inf')
    self.dist[dst] = float('Inf')

  def bellman_ford(self, source):
    """Finds shortest path or detects negative weight cycle in graph.
    
    Args:
      source: Source vertex from which shortest path is required.
    """

    number_of_vrtx = len(self.dist)
    self.dist[source] = 0  # Source is reachable with distance 0.

    # For each vertex, apply relaxation for all edges
    for ctr in range(number_of_vrtx - 1):
      for u, v, w in self.edges:
        if self.dist[v] > self.dist[u] + w:
          self.dist[v] = self.dist[u] + w
    
    # Run algorithm a second time to detect which nodes are part of a negative
    # cycle. A negative cycle has occurred if we can find a better path beyond
    # the optimal solution that is if there is still scope of improvement,
    # there is a negative weight cycle in graph.
    # As the distance will keep on decreasing with each iteration of negative
    # edge cycle(will eventually become negative infinity if loop runs forever)
    for ctr in range(number_of_vrtx - 1):
      for u, v, w in self.edges:
        if self.dist[v] > self.dist[u] + w:
          self.dist[v] = float('-inf')
          print(f'Node {v} is part of negative cycle - undefined shortest path')
    
    for k in self.dist:
      print('Vertex: {} \t Distance: {}'.format(k, self.dist[k]))

print('\n*********** Test case 1 ***********')
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

print('\n*********** Test case 2 ***********')
g1 = Graph()
g1.add_edge(0, 1, -1)
g1.add_edge(1, 0, -1)

g1.bellman_ford(0)

"""
Output:
*********** Test case 1 ***********
Vertex: 0 	 Distance: 0
Vertex: 1 	 Distance: -1
Vertex: 2 	 Distance: 2
Vertex: 3 	 Distance: -2
Vertex: 4 	 Distance: 1

*********** Test case 2 ***********
Node 1 is part of negative cycle - undefined shortest path
Node 0 is part of negative cycle - undefined shortest path
Vertex: 0 	 Distance: -inf
Vertex: 1 	 Distance: -inf
"""
