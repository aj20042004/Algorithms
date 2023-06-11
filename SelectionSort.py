
# Selection sort function

def selectionSort(arr):

    n = len(arr)

    for i in range(0,n-1):

        current_min_distance = i

        for j in range(i+1,n):

            if arr[j] < arr[current_min_distance]:

                current_min_distance = j

        arr[i] , arr[current_min_distance] = arr[current_min_distance] , arr[i]



# main function
arr = [234, 1, 34, 5, 66, 7, 9, 0]
print("the array before sorting: ", arr)
selectionSort(arr)
print("the array after sorting: ", arr )