
# Insertion function
def insertionSort(arr):

    n = len(arr)
    for i in range(1,n):

        j = i

        while arr[j-1] > arr[j] and j > 0:
            arr[j-1] , arr[j] = arr[j] , arr[j-1]
            j -= 1


# Main function
arr = [ 23 , 1 , 456 , 232 , 34 , 56, 55]
print("Array before sorting: ", arr )
insertionSort(arr)
print("Array after sorting: ", arr )

