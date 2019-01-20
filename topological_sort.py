#!/usr/bin/python

# Date: 2017-12-30
#
# Description:
# Find linear topological order of a directed acyclic graph(DAG).
#
# Approach:
# Topological order of DAG is such that if in a graph there is a edge from
# u to v then in topological order, u should be before v.
# Topological sort is not possible if graph is not DAG.
# Performed using DFS and stack.
#
# Applications: Used for dependent job scheduling like makefiles.
#
# Reference:
# https://www.geeksforgeeks.org/topological-sorting/
#
# Complexity: O(V + E)

import collections


class Graph(object):
  """Implement methods to manage graph and find its topological order."""

  def __init__(self):
    """Initialises a dictionary to store adjacency list of each vertex."""
    self.graph = collections.defaultdict(list)

  def add_edge(self, start, end):
    """Adds an edge to graph, updates adjacency list of source vertex."""
    self.graph[start].append(end)

  def topological_sort_util(self, current_node, visited, stack):
    """Performs DFS to find the topological ordering from the current node."""
    
    visited[current_node] = True
    for adjacent_vertex in self.graph[current_node]:
      if self.graph.has_key(adjacent_vertex):
        if not visited[adjacent_vertex]:
          self.topological_sort_util(adjacent_vertex, visited, stack)
        else:
          pass
      else:
          if adjacent_vertex not in stack:
            stack.append(adjacent_vertex)
          else:
            pass
    stack.append(current_node)

  def topological_sort(self):
    """Finds topological ordering of DAG 'self'."""
    
    # Maintain topological order in stack.
    stack = []

    visited = {v : False for v in self.graph}
    for vertex in self.graph:
      if not visited[vertex]:
        self.topological_sort_util(vertex, visited, stack)

    stack.reverse()
    print stack


g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.topological_sort()

# Output: [5, 4, 0, 2, 3, 1]

g1 = Graph()
g1.add_edge(5, 2)
g1.add_edge(6, 2)

g1.topological_sort()

# Output: [6, 5, 2]
