for i in range(5):
    print(i)

print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

for i, v in enumerate(a):
    print(i, v)

print(range(0, 10), '# Behavior of range() is like a list, but range() is not list. We call it \'iterable\'')
print(list(range(0, 10)))
