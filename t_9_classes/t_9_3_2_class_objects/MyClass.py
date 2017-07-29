class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = MyClass()
print(x.f())

c = Complex(3.0, -4.5)
print(c.r)
print(c.i)

