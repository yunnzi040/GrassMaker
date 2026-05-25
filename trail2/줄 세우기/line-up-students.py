n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.
class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

studentss = [Student(students[i][0], students[i][1], i+1) for i in range(n)]

studentss.sort(key=lambda x: (-x.height, -x.weight, x.number))

for student in studentss:
    print(student.height, student.weight, student.number)
