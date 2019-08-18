
'''https://www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/'''


'''
ALGORITHM

1)Find the pivot element of the sorted and the rotated array. The pivot element is the largest element in the array. The smallest element will be adjacent to it.
2)Use two pointers (say left and right) with the left pointer pointing to the smallest element and the right pointer pointing to largest element.
3)Find the sum of the elements pointed by both the pointers.
4)If the sum is equal to x, then increment the count. If the sum is less than x, then to increase sum move the left pointer to next position by incrementing it in a rotational manner. If the sum is greater than x, then to decrease sum move the right pointer to next position by decrementing it in rotational manner.
5)Repeat step 3 and 4 until the left pointer is not equal to the right pointer or until the left pointer is not equal to right pointer – 1.
6)Print final count.'''
def pairsInSortedRotated(arr, n, x):
    for i in range(n):
        if arr[i] > arr[i + 1]:
            break

    # l is index of
    # smallest element.
    l = (i + 1)
    #print("l",l)

    # r is index of
    # largest element.
    r = i
    #print("r",r)

    # Variable to store
    # count of number
    # of pairs.
    cnt = 0
    while (l != r):
        if arr[l] + arr[r] == x:
            cnt += 1

            if l == (r - 1 + n) % n:
                return cnt

            l = (l + 1) % n
            r = (r - 1 + n) % n

        elif arr[l] + arr[r] < x:
            l = (l + 1) % n

        else:
            r = (n + r - 1) % n

    return cnt


# Driver Code
arr = [11, 15, 6, 7, 9, 10]
s = 16

print(pairsInSortedRotated(arr, 6, s))