a, b = map(int, input().split())

# Please write your code here.
def onjeonsu(i):
    return i % 2 != 0 and i % 10 != 5 and not (i % 3 == 0 and i % 9 != 0)
    # True: 모두 만족한 경우 (온전수) False: 온전수 아님

cnt = 0

for i in range(a, b+1):
    if onjeonsu(i):
        cnt += 1

print(cnt)