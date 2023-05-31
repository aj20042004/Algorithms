# Breadth - first Search function

def dfs(graph,visited,Queue,First_Node):

    visited.append(First_Node)
    Queue.append(First_Node)

    while Queue:
        element = Queue.pop(0)
        print(element)

        for child_nodes in graph[element]:
            if child_nodes not in visited:
                visited.append(child_nodes)
                Queue.append(child_nodes)


# Main function
# Dictionary for the representing the graphs
graph = {

    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

First_Node = 'A'
visited = []
Queue = []
print("Breadth First Technique for traversing: ")
dfs(graph,visited,Queue,First_Node)