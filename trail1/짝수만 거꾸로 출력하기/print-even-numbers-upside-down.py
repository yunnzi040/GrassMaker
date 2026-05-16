N = int(input())
numbers = list(map(int,input().split()))
arr = []

for num in numbers:
    if num % 2 == 0 :
        arr.append(num)

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=" ")