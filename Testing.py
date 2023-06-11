
import heapq

# Prim's function

def Prim(graph):

    start_vertex = list(graph.keys())[0]

    priority_queue = [(0,start_vertex)]

    mst = []

    while priority_queue:

        weight , vertex = heapq.heappop(priority_queue)

        if vertex not in mst:
            mst.append(vertex)

            for neigbhour , weight in graph[vertex].items():
                if neigbhour not in mst:
                    heapq.heappush(priority_queue,(weight,neigbhour))

    return  mst


# main function
graph = {
    'A': {'B': 2, 'C':3},
    'B': {'A': 2, 'C': 4, 'D':3},
    'C': {'A': 3, 'B': 4, 'D':5},
    'D': {'B': 3, 'C': 5}
}

mst = Prim(graph)
print("Minimum spanning Tree: ", mst)