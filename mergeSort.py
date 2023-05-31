# mergeSort function
def mergeSort(arr):
    # Checking the length of the array
    if len(arr) > 1:

        # Calculate mid
        mid = len(arr) // 2

        # Initializing left array
        left_array = arr[:mid]
        right_array = arr[mid:]

        # Intializing index variables
        i = 0
        j = 0
        k = 0

        # Sorting the array using recursions
        mergeSort(left_array)
        mergeSort(right_array)

        # Solving
        while i < len(left_array) and j < len(right_array):

            # checking left array is smaller than right array
            if left_array[i] < right_array[j]:

                arr[k] = left_array[i]
                i += 1

            else:
                arr[k] = right_array[j]
                j += 1
            k += 1

        # Solving all the test cases
        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1


# main function
arr = [9, 34, 2, 89, 0, 45, 1]
print("Array before sorting: ", arr)
print(" ")
mergeSort(arr)
print("Array after sorting : ", arr)
