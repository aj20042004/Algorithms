
# Breadth first search function
def dfs(graph,visited,Queue,first_node):

    visited.append(first_node)
    Queue.append(first_node)

    while Queue:

        elements = Queue.pop(0)
        print(elements)

        for neighbours in graph[elements]:
            if neighbours not in visited:
                visited.append(neighbours)
                Queue.append(neighbours)

# Main Function
graph = {

    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

first_node = 'A'
visited = []
Queue = []
dfs(graph,visited,Queue,first_node)















