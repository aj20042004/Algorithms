
# Dijkstra's Algorithm function
def dijkstra(graph,first_node):

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

        for neighbor_1 , neighbor_2 in graph[min_node].items():
            new_dist = distance[min_node] + neighbor_2
            if new_dist < distance[neighbor_1]:
                distance[neighbor_1] = new_dist

    return distance

# main function
graph =  {

    'A': {'B':5,'C':2},
    'B': {'C':1,'A':5},
    'C': {'A':2,'B':1,'D':6},
    'D': {'B':3,'C':6}
}

first_node = 'A'

elements = dijkstra(graph,first_node)

print("Shortest distance from node", first_node + ':')

for node,distance in elements.items():
    print(node , ':' , distance)