arr = list(map(int, input().split()))
result = []

for i in arr:
    result.append(chr(i))

print(*result)