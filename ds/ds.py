S = 'Spam'
#S.find('pa')
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("marix[1]", matrix[2])
print("matrix[1][1]", matrix[2][2])

#list
L = [1]
L[:0] = [2, 3, 4]
print(L)
arr = [1, 2, 3]
arr.extend([5, 7, 6])
arr1 = arr.copy()
#arr.sort()
print(arr1)

#dictionary
D = {'spam': 2, 'ham': 1, 'eggs': 3}
D['ham'] = ['grill', 'bake', 'fry']
#del D['eggs']
D['brunch'] = 'Bacon'
print(D)
print(list(D.items()))
print(D.get('spam'))
D2 = {'toast':4, 'muffin':5}
D.update(D2)
#D.pop()
print(D)

Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
X = 2; Y = 3; Z = 4
print(Matrix[(X, Y, Z)])

#tuples
T = (1, 3, 3, 4, 5, 7, 7, 7, 7, 7, 9)
print("T.index()",T.index(7))
print("T.count()",T.count(7))
print(T)