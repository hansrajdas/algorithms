#!/usr/bin/python

# Date: 2020-12-17
#
# Description:
# Each year, the government releases a list of the 10000 most common baby names
# and their frequencies (the number of babies with that name). The only problem
# with this is that some names have multiple spellings. 
# For example, "John" and "Jon" are essentially the same name but would be
# listed separately in the list. Given two lists, one of names/frequencies and
# the other of pairs of equivalent names, write an algorithm to print a new
# list of the true frequency of each name. Note that if John and Jon are
# synonyms, and Jon and Johnny are synonyms, then John and Johnny are synonyms.
# (It is both transitive and symmetric.) In the final list, any name can be
# used as the "real " name.
#
# EXAMPLE
# Input:
#   Names: John (15), Jon (12), Chris (13), Kris (4), Christopher (19)
#   Synonyms: (Jon, John), (John, Johnny), (Chris, Kris), (Chris, Christopher)
# Output: John (27), Kris (36)
#
# Approach:
# Main challenge is maintain synonym names. To solve, we can use graph and
# add an edge between 2 names if they are synonyms
# In the second part, we can traverse graph using BFS or DFS to print
# consolidated count of synonym names
#
# Complexity:
# O(B + P)
# B = Number of baby name and frequencies
# P = Number of synonym pairs

class GraphNode:
    def __init__(self, name, freq):
        self.name = name
        self.frequency = freq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, name, frequency):
        self.graph[name] = {'frequency': frequency, 'adjacency': []}

    def add_edge(self, name1, name2):
        if name1 in self.graph:
            self.graph[name1]['adjacency'].append(name2)
        if name2 in self.graph:
            self.graph[name2]['adjacency'].append(name1)

def truly_popular_names(names, synonyms):
    graph = construct_graph(names)
    connect_edges(graph, synonyms)

    root_names = get_true_frequencies(graph)
    return root_names

def construct_graph(names):
    graph = Graph()
    for name in names:
        graph.add_node(name, names[name])  # name and frequency 
    return graph

def connect_edges(graph, synonyms):
    for pair in synonyms:
        graph.add_edge(pair[0], pair[1])

def get_true_frequencies(graph):
    """Traverses graph using BFS and returns frequencies of names."""
    frequencies = {}
    visited = set()
    for name in graph.graph:
        if name in visited:
            continue
        frequencies[name] = graph.graph[name]['frequency']
        for adjacent in graph.graph[name]['adjacency']:
            if adjacent in visited:
                continue
            visited.add(adjacent)
            if adjacent in graph.graph:
                frequencies[name] += graph.graph[adjacent]['frequency']
    return frequencies

def main():
    names = {
        'John': 15,
        'Jon': 12,
        'Chris': 13,
        'Kris': 4,
        'Christopher': 19
    }

    synonyms = [
        ('Jon', 'John'),
        ('John', 'Johnny'),
        ('Chris', 'Kris'),
        ('Chris', 'Christopher')
    ]
    print(truly_popular_names(names, synonyms))


if __name__ == '__main__':
    main()
