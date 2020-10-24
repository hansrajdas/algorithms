#!/usr/bin/python

# Date: 2020-10-23
#
# Description:
# Given a list of projects and a list of dependencies(which is a list of pairs
# of projects, where the second project is dependent on the first project). All
# of project's dependencies must be build before the project is. Find a build
# order that will allow the projects to build. If there is no valid build
# order, return an error.
#
# Approach:
# - Build a graph having adjacent vertices as dependents
# - Do topological sort to print correct build order
# - In case created graph has a cycle(has back edge) then build order is not
#   possible
#
# Complexity:
# O(P + D), P is the number of projects and D is the number of dependency pairs

class Graph:
    def __init__(self, nodes):
        self.g = {}
        for node in nodes:
            self.g[node] = []

    def add_dependency(self, depends_on, dependent):
        self.g[dependent].append(depends_on)

    def cycle_wrt_node(self, node, visited):
        visited[node] = True
        for adj in self.g.get(node, []):
            if adj in visited:
                if not visited[adj]:
                    return self.cycle_wrt_node(adj, visited)
                else:
                    raise ValueError(
                        'Project order not possible - have cyclic dependency')

    def has_cycle(self):
        for node in self.g:
            visited = {n: False for n in self.g}
            self.cycle_wrt_node(node, visited)

    def print_topological_order(self, node, visited):
        if node in visited:
            return
        for dep in self.g[node]:
            self.print_topological_order(dep, visited)
        visited.add(node)
        print(node, end=' ')
        
    def print_project_build_order(self):
        self.has_cycle()

        visited = set()
        for node in self.g:
            self.print_topological_order(node, visited)
        print()
        
def main():
    g = Graph(['a', 'b', 'c', 'd', 'e', 'f'])

    g.add_dependency('a', 'd')  # d depends on a
    g.add_dependency('f', 'b')
    g.add_dependency('b', 'd')
    g.add_dependency('f', 'a')
    g.add_dependency('d', 'c')

    g.print_project_build_order()

main()  # f a b d c e
