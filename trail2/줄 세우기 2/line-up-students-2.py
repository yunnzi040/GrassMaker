n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.

class Student:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

studentss = [Student(students[i][0], students[i][1], students[i][2]) for i in range(n)]

studentss.sort(key=lambda x: (x.height, -x.weight))

for student in studentss:
    print(student.height, student.weight, student.num)
