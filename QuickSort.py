# Quick Sort function
def quickSort(arr, left, right):
    # Checking whether array has at least two elements
    if left < right:
        # Finding the pivot element
        pivot_element = pivot(arr, left, right)
        quickSort(arr, left, pivot_element - 1)
        quickSort(arr, pivot_element + 1, right)


# Function for finding the pivot element
def pivot(arr, left, right):
    # Defining variables
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1

        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


# Main Function
arr = [234, 1, 34, 5, 66, 7, 9, 0]
print("array before sorting", arr)
quickSort(arr, 0, len(arr) - 1)
print("array after sorting", arr)