t = 12345, 54321, 'hello!'
print(t)
print(t[0])

u = t, (1, 2, 3, 4, 5)
print(u)

# t[0] = 88888 # Tuple is immutable.
v = [1, 2, 3], [3, 2, 1]
print(v)
v[0][1] = 2222 # List in tuple is mutable.
print(v)

empty = ()
singleton = 'hello',
print(len(empty))
print(len(singleton))
print(singleton)

x, y, z = t
# x1, y1 = t # Unpacking of tuple need amount of variables which is same with amount of tuple element.
print(x)
print(y)
print(z)

