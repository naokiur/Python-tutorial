squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:])

# This is shallow copy
squares_2 = squares[:]
print(squares_2 + [36, 49, 64, 81, 100])
print(squares_2)

print('squares_2[0] = 0')
squares_2[0] = 0
print('squares :', squares)
print('squares_2 :', squares_2)
print('squares[0] = 10')
squares[0] = 10
print('squares :', squares)
print('squares_2 :', squares_2)

cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 64
print(cubes)
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)

letters[:] = []
print(letters)

letters = ['A', 'B', 'C']
print(letters)
letters = []
print(letters)

letters = ['a', 'b', 'c', 'd']
print(len(letters))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
