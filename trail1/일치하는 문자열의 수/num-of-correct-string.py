a, A = map(str, input().split())
n = int(a)
cnt = 0

for _ in range(n):
    word = input()
    if word == A:
        cnt += 1

print(cnt)
