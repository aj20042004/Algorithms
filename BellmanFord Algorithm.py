

# Intialize function
def initialize(graph, first_node):

    distance = {}
    tracking_prev = {}

    for node in graph:
        distance[node] = float('inf')
        tracking_prev[node] = None

    distance[first_node] = 0

    return distance , tracking_prev


# relax function
def relax(key,second_key,weight , distance, tracking_prev):

    if distance[second_key] > distance[key] + weight:

        distance[second_key] = distance[key] + weight
        tracking_prev[second_key] = key


# Bellman Ford function
def BellmanFord(graph , first_node):

    distance , tracking_prev = initialize(graph , first_node)

    for times in range(len(graph)-1):

        for key in graph:
            for second_key in graph[key]:
                weight = graph[key][second_key]
                relax(key,second_key,weight, distance,tracking_prev)

        for key in graph:
            for second_key in graph[key]:
                weight = graph[key][second_key]
                if distance[second_key] > distance[key] + weight:
                    raise Exception("Negative loop cycle exists")

    return distance , tracking_prev


# main function
graph = {
    'A': {'B': 3, 'C': 5},
    'B': {'C': 1, 'D': -2},
    'C': {'D': 4},
    'D': {'A': 2},
}

first_node = 'A'

distance , tracking_prev = BellmanFord(graph , first_node)

for node in distance:
    print("Node :", node , "distance:" ,distance[node] )

