
def bubbleSort(arr):

    n = len(arr)
    swapped = False

    for i in range(n-1):

        for j in range(0,n-i-1):

            while arr[j] > arr[j+1]:

                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swapped = True
        if not swapped:
            return


def insertionSort(arr):

    n = len(arr)

    for i in range(1,n):

        j = i

        while arr[j-1] > arr[j] and j > 0:

            arr[j-1] , arr[j] = arr[j] , arr[j-1]
            j -= 1

def selectionSort(arr):

    n = len(arr)

    for i in range(n-1):

        current_min = i

        for j in range(i+1,n):

            while arr[j] < arr[current_min]:
                current_min = j

        arr[i] , arr[current_min] = arr[current_min] , arr[i]


def MergeSort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2
        left_array = arr[:mid]
        right_array = arr[mid:]

        i = 0
        j = 0
        k = 0

        MergeSort(left_array)
        MergeSort(right_array)

        while i < len(left_array) and j < len(right_array):

            if left_array[i] < right_array[j]:

                arr[k] = left_array[i]
                i += 1

            else:
                arr[k] = right_array[j]
                j += 1

            k += 1

        while i < len(left_array):

            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):

            arr[k] = right_array[j]
            j += 1
            k += 1

def quickSort(arr,left,right):

    if left < right:

        pivot_element = pivot(arr,left,right)
        quickSort(arr,left,pivot_element-1)
        quickSort(arr,pivot_element+1,right)


def pivot(arr, left, right):

    i = left
    j = right - 1
    pivot_num = arr[right]

    while i < j:

        while i < right and arr[i] < pivot_num:
            i += 1

        while j > left and arr[j] >= pivot_num:
            j -= 1

        if i < j:
            arr[i] , arr[j] = arr[j] , arr[i]

    if arr[i] > pivot_num:

        arr[i] , arr[right] = arr[right] , arr[i]

    return i


def binarySearch(arr,target):

    begin = 0
    end = len(arr) - 1

    while begin <= end:

        mid = begin + end // 2
        midVal = arr[mid]

        if target == midVal:
            return "Element found"

        elif target < midVal:
            end = mid - 1

        elif target > midVal:
            begin = mid + 1

    return "Element not found"


def linearSearch(arr,target):

    n = len(arr)

    for i in range(0,n):

        if arr[i] == target:
            return "element found......."

    return "element not found"


def BFS(graph,first_node,visited,queue):

    visited.append(first_node)
    queue.append(first_node)

    while queue:
        element = queue.pop(0)
        print(element, end=' ')

        for child_nodes in graph[element]:
            if child_nodes not in visited:
                visited.append(child_nodes)
                queue.append(child_nodes)


def DFS(graph,first_node):

    visited = set()

    stack = [first_node]

    while stack:

        element = stack.pop()

        if element not in visited:

            print(element, end=" ")

            visited.add(element)

            stack.extend(graph[element] - visited)

# Main function
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

first_node = 'A'
DFS(graph,first_node)


















#arr = [1 , 34 , 56 ,78, 90 ]
#print(linearSearch(arr,56))