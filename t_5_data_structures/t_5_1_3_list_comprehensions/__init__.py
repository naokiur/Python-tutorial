from math import pi

squares1 = []

for x in range(10):
    squares1.append(x ** 2)
print(squares1)
print("Still exists 'x' : ", x)

squares2 = list(map(lambda x:x ** 2, range(10)))
print(squares2)
squares3 = [x ** 2 for x in range(10)]
print(squares3)

combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs)

vec1 = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec1])
print([x for x in vec1 if x >= 0])
print([abs(x) for x in vec1])

freshFruit = [' banana', ' logan berry ', 'passion fruit ']
print([weapon.strip() for weapon in freshFruit])
print([(x, x ** 2) for x in range(6)])
# print([x, x ** 2 for x in range(6)]) # The tuple must be parenthesized.

vec2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elm in vec2 for num in elm])

print([str(round(pi, i)) for i in range(1, 6)])
