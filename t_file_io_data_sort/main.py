class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


with open("students.txt") as file:
    student_list = []

    for line in file:
        record = line.split(",")
        student_list.append(Student(record[0], int(record[1])))

    file.close()

# first resolution
max_student_name = ""
max_student_score = 0
for student in student_list:
    if max_student_score < student.score:
        max_student_score = student.score
        max_student_name = student.name

print(max_student_name)

# second resolution
max_student = max(student_list, key=(lambda s: s.score))
print(max_student.name)

min_student = min(student_list, key=(lambda s: s.score))
print(min_student.name)