#!/usr/bin/python

# Date: 2020-12-29
#
# Description:
# Print set of connected components in a graph.
# All vertices reachable from a node is called a connected component.
#
# Approach:
# Start from a node and do DFS to traverse graph, all nodes which are reachable
# from that node is a connected component - save them as a list corresponding
# to a connected component id like 0, 1, 2...
#
# Complexity:
# O(V + E)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dst):
        if src in self.graph:
            self.graph[src].append(dst)
        else:
            self.graph[src] = [dst]

    def dfs(self, node, visited, component_num, connected_components):
        visited.add(node)
        if component_num not in connected_components:
            connected_components[component_num] = []
        connected_components[component_num].append(node)
        
        for next_node in self.graph.get(node, []):
            if next_node not in visited:
                self.dfs(next_node, visited, component_num, connected_components)

    def find_connected_components(self):
        visited = set()
        connected_components = {}
        component_num = 0
        for node in self.graph:
            if node not in visited:
                component_num += 1
                self.dfs(node, visited, component_num, connected_components)

        # Print connected components
        for count in connected_components:
            print(f'Connected component {count}: {connected_components[count]}')

def main():
    g = Graph()
    g.add_edge(10, 11)
    g.add_edge(10, 12)
    g.add_edge(11, 13)
    g.add_edge(13, 14)
    g.add_edge(15, 16)

    g.find_connected_components()

if __name__ == '__main__':
    main()


# Output:
# -------
# Connected component 1: [10, 11, 13, 14, 12]
# Connected component 2: [15, 16]
