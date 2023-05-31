# LinearSearch function
def LinearSearch(arr,target):

    # Calculating the length of array
    n = len(arr)

    # iterating one by one to check whether element equal to target
    for i in range(0,n):
 
        if arr[i] == target:
            return "Element found at index", i
        
    return "Sorry cannont find the element"


# main function
arr = [9,10,23,45]
print("This is my array",arr)
ch = int(input("Which number to search: "))
print(LinearSearch(arr,ch))
