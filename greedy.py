'''https://www.geeksforgeeks.org/maximum-product-subset-array/'''
import math
import heapq

def maxProdSubset(arr,n):
    if n ==1:
        return arr[0]

    max_neg = -999999999999
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range(n):
        if arr[i]==0:
            count_zero += 1
        if arr[i]<0:
            count_neg+= 1
            max_neg = max(max_neg,arr[i])
            print("max_neg at",i, max_neg)

        prod = prod * arr[i]
        print("prod at",i, prod)

    if count_zero == n:
        return 0
    if count_neg %2 == 1:
        if count_neg == 1 and count_zero > 0 and count_zero+count_neg == n:
            return  0
        print("max_neg finally",max_neg)
        prod1 = prod / max_neg

    return prod1

def minProdSubset(arr,n):
    if (n == 1):
        return arr[0]
    max_neg = float('-inf')
    print(max_neg)
    min_pos = float('inf')
    print(min_pos)
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range(n):
        if (arr[i]) == 0:
            count_zero += 1
        if (arr[i]<0):
            count_neg += 1
            max_neg = max(max_neg,arr[i])
            print("value of max_neg at",i ,max_neg)
        if(arr[i] > 0):
            min_pos = min(min_pos,arr[i])
        prod = prod * arr[i]
    if count_zero == n or (count_neg == 0 and count_zero >0):
        return 0;
    if (count_neg == 0):
        return min_pos
    if (count_neg & 1) == 0 and count_neg != 0:
        prod = int(prod / max_neg)
    return prod

def maxsum_after_K_negations(arr,n,k):
    minPos = 99999999
    sum = 0
    index = -1
    for i in range(n):
        if(k<0):
            break
        if(arr[i] < 0):
            arr[i]= -arr[i]
            k = k -1
        if(arr[i]<minPos and arr[i]>-1):
            minPos = arr[i]
            index = i
            print("index",index,"minPos",minPos,"at i",i)
        sum +=arr[i]
    for i in range(k):
        arr[index]=-arr[index]
        sum+=(2*arr[index])
    return sum

'''https://www.geeksforgeeks.org/maximum-sum-increasing-order-elements-n-arrays/'''

M = 4
def maxSum_from_n_array(arr,n):
    prev = max(max(arr))
    sum = prev
    for i in range(n-2,-1,-1):
        print(i)
        max_smaller = -10**9
        for j in range(M-1,-1,-1):
            if arr[i][j] < prev and arr[i][j] > max_smaller:
                max_smaller = arr[i][j]
            if max_smaller == -10**9:
               return 0
        prev = max_smaller
        sum += max_smaller
    return sum


'''https://www.geeksforgeeks.org/maximum-sum-absolute-difference-array/'''
'''
To get the desired result we follow the steps below:
1)arrange the array in a way such that smallest and largest elements come alternatively
2)get the sum
'''
def MaximumHeight(a, n):
    return (-1 + int(math.sqrt(1 +
                    (8 * n)))) // 2

'''https://www.geeksforgeeks.org/find-maximum-height-pyramid-from-the-given-array-of-objects/'''
def maxLevel(boxes, n):
    # Sort objects in increasing
    # order of widths
    boxes.sort()

    ans = 1  # Initialize result

    # Total width of previous
    # level and total number of
    # objects in previous level
    prev_width = boxes[0]
    prev_count = 1

    # Number of object in
    # current level.
    curr_count = 0

    # Width of current level.
    curr_width = 0
    for i in range(1, n):

        # Picking the object. So
        # increase current width
        # and number of object.
        print("i",i,"\n")
        print("boxes[i]",boxes[i],"\n")
        curr_width += boxes[i]
        print("curr_width",curr_width,"\n")
        curr_count += 1
        print("curr_count",curr_count,"\n")

        # If current width and
        # number of object are
        # greater than previous.
        if (curr_width > prev_width and
                curr_count > prev_count):
            # Update previous width,
            # number of object on
            # previous level.
            prev_width = curr_width
            prev_count = curr_count

            # Reset width of current
            # level, number of object
            # on current level.
            curr_count = 0
            curr_width = 0

            # Increment number of level.
            ans += 1
            print("level",ans)
    return ans


def Max_difference(arr,N,K):
    S=0
    S1=0

    for i in range(N):
        S += arr[i]
    M = max(k, N - k)
    l1 = heapq.nlargest(M,arr)
    for i in range(M):
        list(l1)
        S1 += l1[i]
    max_difference = S1 - (S - S1)
    return max_difference


def maxDifference(arr, N, k):
    S = 0
    S1 = 0
    maxdifference = 0

    # Sum of the array
    for i in range(N):
        S += arr[i]

        # Sort the array in descending order
    arr.sort(reverse=True)
    M = max(k, N - k)
    for i in range(M):
        S1 += arr[i]

        # Calculating max_difference
    maxdifference = S1 - (S - S1)
    return maxdifference

'''https://www.geeksforgeeks.org/minimum-sum-product-two-arrays/'''
def minproduct(a, b, n, k):
    diff = 0
    res = 0
    for i in range(n):

        # Find product of current
        # elements and update result.
        pro = a[i] * b[i]
        res = res + pro

        # If both product and
        # b[i] are negative,
        # we must increase value
        # of a[i] to minimize result.
        if (pro < 0 and b[i] < 0):
            temp = (a[i] + 2 * k) * b[i]

            # If both product and
        # a[i] are negative,
        # we must decrease value
        # of a[i] to minimize result.
        elif (pro < 0 and a[i] < 0):
            temp = (a[i] - 2 * k) * b[i]

            # Similar to above two cases
        # for positive product.
        elif (pro > 0 and b[i] < 0):
            temp = (a[i] + 2 * k) * b[i]
        elif (pro > 0 and a[i] > 0):
            temp = (a[i] - 2 * k) * b[i]

            # Check if current difference
        # becomes higher
        # than the maximum difference so far.
        d = abs(pro - temp)

        if (d > diff):
            diff = d
    return res - diff
'''https://www.geeksforgeeks.org/minimum-sum-choosing-minimum-pairs-array/'''
''' 
  There is an easy trick to solve this question and that is always choose the smallest element of array A[] and its adjacent, delete the adjacent element and copy smallest one to array B[]. Again for next iteration we have same smallest element and any random adjacent element which is to be deleted. After n-1 operations all of elements of A[] got deleted except the smallest one and at the same time array B[] contains “n-1” elements and all are equal to smallest element of array A[]
  Thus total sum of array B[] is equal to smallest * (n-1)
 '''
def minSum(A):
    min_val = min(A)

    return min_val* (len(A)-1)




if __name__ =="__main__":

    #arr = [-2, 0, 5, -1, 2]
    #n = len(arr)
    #k=4
    #print(minProdSubset(arr,n))
    #print(maxsum_after_K_negations(arr,n,k))
    #arr = [[1, 7, 3, 4],
    #       [4, 2, 5, 1],
    #      [9, 5, 1, 8]]
    #n = len(arr)
    #print(maxSum_from_n_array(arr, n))

    #arr = [40, 100, 20, 30]
    #n = len(arr)
    #print(MaximumHeight(arr, n))

    #boxes = [10, 20, 30, 50, 60, 70]
    #n = len(boxes)
    #print(maxLevel(boxes, n))

    #arr1 = [8, 4, 5, 2, 10]
    #N = len(arr)
    #k = 2
    #print(maxDifference(arr1, N, k))
    #print(Max_difference(arr1, N, k))
    a = [2, 3, 4, 5, 4]
    b = [3, 4, 2, 3, 2]
    n = 5
    k = 3
    print(minproduct(a, b, n, k))
    A = [7, 2, 3, 4, 5, 6]
    print (minSum(A))