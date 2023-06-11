
# Depth first Search function
def dfs(graph,first_node):

    "Creating a list for tracking visited nodes"
    visited = set()

    "Creating stack for traversing"
    stack = [first_node]

    while stack:

        element = stack.pop()

        if element not in visited:
            print(element, end = " ")

            # Adding elements visited
            visited.add(element)

            # Adding all the adjacent nodes to stack
            stack.extend(graph[element] - visited )


# main function
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

first_node = 'A'
dfs(graph,first_node)

