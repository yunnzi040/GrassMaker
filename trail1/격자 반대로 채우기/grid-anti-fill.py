n = int(input())

arr_2d = [[0 for _ in range(n)] for _ in range(n)]

num = n * n

# n이 짝수일 때, 첫줄이 아래서부터 위로
if n % 2 != 0:
    for i in range(n):
        if i % 2 == 1: # 홀수번째 줄일 때
            for j in range(n-1, -1, -1): # 3, 2, 1
                arr_2d[j][i] = num
                num -= 1
        else:
            for j in range(n):
                arr_2d[j][i] = num
                num -= 1
        

# n이 홀수일 때, 첫줄이 위에서부터 아래로
else: 
    for i in range(n): # 0, 1, 2
        if i % 2 == 1:
            for j in range(n):
                arr_2d[j][i] = num
                num -= 1
        else:
            for j in range(n-1, -1, -1): # 3, 2, 1
                arr_2d[j][i] = num
                num -= 1



for row in arr_2d:
    print(*row)