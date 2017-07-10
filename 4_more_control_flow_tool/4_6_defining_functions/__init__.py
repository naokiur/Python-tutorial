def feb(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

# Print None.
print(feb(2000))


def feb2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

print(feb2(200))

arg = 0


def add(n):
    """Add 1."""
    return n + 1

print('Call Function \'add\' with arg:', add(arg))
print('Print arg. Arguments of function is call by value:', arg)
