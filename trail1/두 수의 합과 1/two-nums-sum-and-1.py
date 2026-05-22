a, b = map(int,input().split())
total = str(a+b)
cnt = 0

for i in total:
    if i == '1':
        cnt += 1

print(cnt)


