
# Union Find class

class UnionFind:
    def __init__(self,vertices):

        self.parents = {}
        self.rank = {}

        for node in vertices:
            self.parents[node] = node
            self.rank[node] = 0

    def find(self,node):

        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]


    def union(self,node,neighbour):

        root1 = self.find(node)
        root2 = self.find(neighbour)

        if root1 != root2:

            if self.rank[root1] < self.rank[root2]:
                self.parents[root1] = root2

            elif self.rank[root2] < self.rank[root1]:
                self.parents[root2] = root1

            else:
                self.parents[root2] = root1
                self.rank[root1] += 1


def kruskal(graph):
    minimum_spanning_tree = []
    vertices = set(graph.keys())
    edges = []

    for node in graph:
        for neighbour, weight in graph[node].items():
            edges.append((weight, node, neighbour))

    edges.sort()

    # Initializing the parents and rank in Union Find class
    uf = UnionFind(vertices)

    for weight, node, neighbour in edges:
        if uf.find(node) != uf.find(neighbour):
            minimum_spanning_tree.append((node, neighbour, weight))
            uf.union(node, neighbour)

    return minimum_spanning_tree



# main function
graph = {
    'A': {'B': 2, 'D': 5},
    'B': {'A': 2, 'C': 1, 'D': 3},
    'C': {'B': 1,'D': 4},
    'D': {'A': 5, 'B': 3, 'C': 4},
}

minimum_spanning_tree = kruskal(graph)

print(minimum_spanning_tree)



