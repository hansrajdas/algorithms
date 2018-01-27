#!/usr/bin/python

# Date: 2018-01-27
#
# Description:
# Dijkstra's algo can be used to find shortest path from a source to destination
# in a graph. Graph can have cycles but negative edges are not allowed to use
# dijkstra algo.
#
# Implementation:
# - Initialze graph such that distance to source is set to 0 and other node is
#   reachable from source with infinite distance.
# - Push all vertexes in a priority(distance 0 means highest priority) queue and
#   iterate over queue till queue is empty.
# - In each iteration check and update distance of all adjacent vertexes of
#   fetched vertex from queue.
# - When loop completes we will get shortest path from source to all reachable
#   vertex and non reachable remains infinite as initialized.
#
# Complexity: O(E + VlogV) if fibonacci heap is used to implement priority
# queue.


# Pending :(
