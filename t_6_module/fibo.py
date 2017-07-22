# Fibonacci numbers module


def write_fibo(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def create_fibo(n):
    result = []
    a, b = 0, 1
    while b < n :
        result.append(b)
        a, b = b, a + b
    return result

