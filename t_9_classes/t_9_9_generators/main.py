def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

for char in reversed("maps"):
    print(char)


def adding(max_num):
    result = 0
    for index in range(0, max_num):
        result += index
        yield result

for num in adding(10):
    print(num)
