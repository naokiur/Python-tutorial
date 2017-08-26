for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one': 1, 'two': 2}:
    print(key)
for char in '123':
    print(char)
for line in open("myfile.txt"):
    print(line, end='')

fruits = {'1': 'apple', '2': 'lemon', '3': 'pine'}
for key in fruits:
    print(key, fruits.get(key))

print("Confirmation of Iterator object.")

s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) This will be StopIteration.

class Reverse:
    """Iterator for looping over a sequence back words"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse("spam")
iter(rev)

for char in rev:
    print(char)
