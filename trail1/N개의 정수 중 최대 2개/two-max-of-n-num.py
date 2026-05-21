n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
result = []

for _ in range(2):
    max_val = a[0]
    for i in a[1:]:
        if max_val < i:
            max_val = i
    result.append(max_val)
    a.remove(max_val)

print(*result)


