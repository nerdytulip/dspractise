def largestNumber(array):
    # extval is a empty list for extended
    # values and ans for calculating answer
    extval, ans = [], ""

    # calculating the length of largest number
    # from given and add 1 for further operation
    #print(str(max(array)))
    l = len(str(max(array))) + 1

    # iterate given values and
    # calculating extended values
    for i in array:
        temp = str(i) * l
        #print(temp[:l])
        #print(i)

        # make tuple of extended value and
        # equivalant original value then
        # append to list
        extval.append((temp[:l], i))
        #print(extval)

        # sort extval in descending order
    extval.sort(reverse=True)
    #print(extval)

    # iterate extended values
    for i in extval:
        # concatinate original value equivalant
        # to extended value into ans variable
        ans += str(i[1])
        #print(ans)

    return ans


# Driver code
a = [1, 34, 3, 98, 9, 76,
     45, 4, 12, 121]

print(largestNumber(a))
