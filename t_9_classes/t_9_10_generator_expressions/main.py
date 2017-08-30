from math import pi, sin

print(sum(i * i for i in range(10)))

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x * y for x, y in zip(xvec, yvec)))

sine_table = {x: sin(x * pi / 180) for x in range(0, 91)}
print(sine_table)

page = open("myfile.txt")
unique_words = set(word for line in page for word in line.split())
print(unique_words)


class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

graduates = [Student("john", 4.0), Student("helen", 4.2), Student("jack", 3.0)]

valedictorian = max((student.gpa, student.name) for student in graduates)
print(valedictorian)

data = "golf"
print(list(data[i] for i in range(len(data) - 1, -1, -1)))
