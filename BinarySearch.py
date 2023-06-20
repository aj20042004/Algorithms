#binarySearch function
def binarySearch(arr,element):

    begin = 0
    end = len(arr) - 1

    while begin <= end:

        mid = begin + end // 2
        midVal = arr[mid]


        if midVal == element:

            return "Element found in array at index", mid 

        elif element < midVal:

            end = mid - 1

        elif element > midVal:

            begin = mid + 1

    return "Sorry ! element not found in the array"

#main function
arr = [233 , 0 , 90 , 1 ,2 , 55]
print("Thsi is our array  : " , arr)
ch = int(input("What value to search ? : "))
print(binarySearch(arr,ch))



