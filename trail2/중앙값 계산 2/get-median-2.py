n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def print_mid(_list):
    _list = sorted(_list)
    mid = (len(_list)) // 2

    return _list[mid]

result = []

for i in range(len(arr)):
    if i == 0:
        result.append(arr[0])
    elif i % 2 == 0:
        result.append(print_mid(arr[:i+1]))

print(*result)
    

