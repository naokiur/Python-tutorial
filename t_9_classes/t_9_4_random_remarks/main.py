def f1(self, x, y):
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


c1 = C()
print(c1.g())
print(c1.h())
print(c1.f(1, 2))


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.data.append(x)
        self.data.append(x)


bag1 = Bag()
bag1.add(1)
bag1.addtwice(2)

print(bag1.data)

