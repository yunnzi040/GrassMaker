n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
result = []
k = len(a)

while k > 0:
    arr = a[:k]
    max_index = arr.index(max(arr))
    result.append(max_index+1)
    k = max_index

print(*result)