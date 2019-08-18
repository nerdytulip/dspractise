'''https://www.geeksforgeeks.org/rearrange-array-arri-arrj-even-arri/
Input : arr[] = {1, 2, 3, 4, 5, 6, 7}
Output : 4 5 3 6 2 7 1
'''

def arrange_array(arr, n):
    evenpos = int(n/2)
    print(evenpos)
    oddpos = n - evenpos
    print(oddpos)

    temp = list()

    for i in range(0, n):
        temp.append(arr[i])

    j= evenpos
    for i in range(0,n,2):
        arr[i]= temp[j]
        j = j-1

    k= oddpos
    for i in range(1,n,2):
        arr[i]= temp[k]
        k = k + 1
    print(arr)


if __name__ =="__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    arrange_array(arr, n)
