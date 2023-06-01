
def dijkstra( graph , first_node):

    distance = {}
    for node in graph:
        distance[node] = float('inf')
    distance[first_node] = 0

    visited = []

    while len(visited) < len(graph):

        min_dist = float('inf')
        min_node = None

        for node in graph:
            if node not in visited and distance[node] < min_dist:
                min_dist = distance[node]
                min_node = node

        visited.append(min_node)

        for neighbour, weight in graph[min_node].items():
            new_dist = distance[min_node] + weight
            if new_dist < distance[neighbour]:
                distance[neighbour] = new_dist

    return distance


# main function
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 6},
    'D': {'B': 1, 'C': 6}
}

first_node = 'A'

elements = dijkstra(graph,first_node)

for neighbour, weight in elements.items():
    print(neighbour,":", weight)
