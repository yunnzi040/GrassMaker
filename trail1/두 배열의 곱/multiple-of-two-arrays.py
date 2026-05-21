arr_2d1 = [
    list(map(int, input().split()))
    for _ in range(3)
]

input()

arr_2d2 = [
    list(map(int, input().split()))
    for _ in range(3)
]

result = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        result[i][j] = arr_2d1[i][j] * arr_2d2[i][j]

for row in result:
    for elem in row:
        print(elem, end=" ")
    print()