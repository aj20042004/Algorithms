

# QuickSort function
def quickSort(arr,left,right):

    if left < right:

        pivot_element = pivot(arr,left,right)
        quickSort(arr,left,pivot_element-1)
        quickSort(arr,pivot_element+1,right)

def pivot(arr,left,right):

    i = left
    j = right - 1
    pivot_number = arr[right]

    while i < j:

        while i < right  and arr[i] < pivot_number:
            i += 1

        while j > left and arr[j] >= pivot_number:
            j -= 1

        if i < j:
            arr[i] , arr[j] = arr[j] , arr[i]

    if arr[i] > pivot_number:
        arr[i] , arr[right] = arr[right] , arr[i]

    return i




# main function
arr = [234, 1, 34, 5, 66, 7, 9, 0]
print("The array before sorting: ", arr)
quickSort(arr,0,len(arr)-1)
print("The array after sorting: ", arr)
