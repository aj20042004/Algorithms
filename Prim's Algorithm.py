
import heapq

# Prim's Function
def Prim(graph):

    start_vertex = list(graph.keys())[0]

    priority_queue = [(0,start_vertex)]

    mst = []
    mst_weight = []

    while priority_queue:

        weight , node = heapq.heappop(priority_queue)

        if node not in mst:
            mst.append(node)
            mst_weight.append(weight)

            for neighbour , weight in graph[node].items():
                if neighbour not in mst:
                    heapq.heappush(priority_queue, (weight,neighbour))

    return mst , mst_weight



# main function
graph = {
    'A': {'B': 2, 'C':3},
    'B': {'A': 2, 'C': 4, 'D':3},
    'C': {'A': 3, 'B': 4, 'D':5},
    'D': {'B': 3, 'C': 5}
}

mst , mst_weight = Prim(graph)

print("The minimum spanning Tree: " , mst )
print("Weight for calculating minimum distance: ", mst_weight)