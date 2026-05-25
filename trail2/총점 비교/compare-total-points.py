n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.
class Student:
    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c

students = [Student(name[i], score1[i], score2[i], score3[i]) for i in range(n)]

students.sort(key=lambda x: x.a + x.b + x.c)

for student in students:
    print(student.name, student.a, student.b, student.c)