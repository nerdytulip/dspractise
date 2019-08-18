'''https://www.geeksforgeeks.org/move-zeroes-end-array-set-2-using-single-traversal/'''
def moveZerosToEnd(arr, n):
    # Count of non-zero elements
    count = 0;

    # Traverse the array. If arr[i] is non-zero, then
    # swap the element at index 'count' with the
    # element at index 'i'
    for i in range(0, n):
        if (arr[i] != 0):
            arr[count], arr[i] = arr[i], arr[count]
            count += 1

''' https://www.geeksforgeeks.org/minimum-swaps-required-bring-elements-less-equal-k-together/ '''


# function to print the array elements
def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")

    # Driver program to test above
if __name__ =="__main__":

 arr = [0, 1, 9, 8, 4, 0, 0, 2,
       7, 0, 6, 0, 9]
 n = len(arr)

 print("Original array:", end=" ")
 printArray(arr, n)

 moveZerosToEnd(arr, n)

 print("\nModified array: ", end=" ")
 printArray(arr, n)