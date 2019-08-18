
'''juggling algorithm for array rotation'''
'''
Time complexity : O(n)
Auxiliary Space : O(1)'''
def juggling_leftRotate(arr, d, n):
    g_c_d = gcd(d, n)
    for i in range(g_c_d):

        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = (j + d)% n
            # if k >= n:
            #     k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


'''block swap algorithm for array rotation

Time complexity : O(n)
Auxiliary Space : O(1)
#algorithm:
we break the array into two parts A and B on the basis of value of d 
initialize A[0..d-1] and B[d...n-1]
a)loop until size of A== size of B 
  i)if A < B , then divide B in two parts Bl and Br (ABlBr)such that size of Br equals size of A ,then swap Br and A 
    such that BrBlA.Now A is at its final place, so recur on pieces of B.
  ii)if A>B,then divide AlArB,such that size of B equals Al,then swap Al and B ,so that now array becomes BArAl.Now B
       is at its final place, so recur on pieces of A.
b)Finally when A and B are of equal size, block swap them.
'''


def blockswap_leftRotate(arr, d, n):
    if (d == 0 or d == n):
        return
    i = d
    j = n - d
    while i != j:

        if i < j:  # A is shorter,A<B
            swap(arr, d - i, d + j - i, i)
            j -= i

        else:  # B is shorter,A>B
            swap(arr, d - i, d, j)
            i -= j

    swap(arr, d - i, d, i)


def swap( arr, fi, si, d):

 for i in range(d):
    temp = arr[fi + i]
    arr[fi + i] = arr[si + i]
    arr[si + i] = temp


def reversal_rotate_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1


def left_rotate(arr, d):
    n = len(arr)
    reversal_rotate_array(arr, 0, d-1) #Ar
    reversal_rotate_array(arr, d, n-1) #Br
    reversal_rotate_array(arr, 0, n-1) #(ArBr)r==AB


# Function to right rotate arr
# of size n by d
def right_rotate(arr, d, n):
    reversal_rotate_array(arr, 0, n - 1)#reverse AB -> BA
    reversal_rotate_array(arr, 0, d - 1)#BrA
    reversal_rotate_array(arr, d, n - 1)#BrAr

# function to print an array
def print_array(arr, size):
    for i in range(size):
        print("% d" % arr[i], end=" ")

    # Function to get gcd of a and b


'''https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/'''

def cyclically_rotate_array(arr):
    n = len(arr)
    x = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1];

    arr[0] = x;


def search_in_sorted_rotated(arr, l, h, key):
    '''Search an element in sorted and rotated array using
     single pass of Binary Search

     Returns index of key in arr[l..h] if key is present,
     otherwise returns -1 '''
    if l > h:
        return -1

    mid = (l + h) // 2
    if arr[mid] == key:
        return mid

        # If arr[l...mid] is sorted
    if arr[l] <= arr[mid]:

        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if key >= arr[l] and key <= arr[mid]:
            return search_in_sorted_rotated(arr, l, mid - 1, key)
        return search_in_sorted_rotated(arr, mid + 1, h, key)

        # If arr[l..mid] is not sorted, then arr[mid... r]
    # must be sorted
    if key >= arr[mid] and key <= arr[h]:
        return search_in_sorted_rotated(arr, mid + 1, h, key)
    return search_in_sorted_rotated(arr, l, mid - 1, key)

def sum_in_rotated_and_sorted(arr,key):
    n = len(arr1)
    x = key

    for i in range(0, n - 1):
        if (arr[i] > arr[i + 1]):
            break;

            # l is now index of smallest element
    l = (i + 1) % n
    # r is now index of largest element
    r = i

    # Keep moving either l
    # or r till they meet
    while (l != r):

        # If we find a pair with
        # sum x, we return True
        if (arr[l] + arr[r] == x):
            return True;

            # If current pair sum is less,
        # move to the higher sum
        if (arr[l] + arr[r] < x):
            l = (l + 1) % n;
        else:

            # Move to the lower sum side
            r = (n + r - 1) % n;

    return False;

''' https://www.geeksforgeeks.org/quickly-find-multiple-left-rotations-of-an-array/'''
def multiple_rotations_in_minimum_time(arr,n,k):
    for i in range(k,n+k):
        print(str(arr[i % n]),end=" ")





        # Driver program to test above functions
if __name__ =="__main__":

 arr = [1, 2, 3, 4, 5, 6, 7]
 juggling_leftRotate(arr,2,7)
 #blockswap_leftRotate(arr,2,7)
print_array(arr, 7)
arr1 = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 6
i = search_in_sorted_rotated(arr1, 0, len(arr) - 1, key)
if i != -1:
    print("Index: %d" % i)
else:
 print("Key not found")

 key= 10

sum_in_rotated_and_sorted(arr1,key)
left_rotate(arr, 2)

multiple_rotations_in_minimum_time(arr,7,2)