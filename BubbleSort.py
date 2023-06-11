
# Bubble sort function
def bubbleSort(arr):

    # Finding h
    n = len(arr)
    swapped = False

    for i in range(n-1):

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True

        if not swapped:

            return

# main function
arr = [ 23 , 1 , 456 , 0 , 34 , 56, 55]

print("Array before sorting: " , arr)
bubbleSort(arr)

print("Array after sorting : ", arr)

