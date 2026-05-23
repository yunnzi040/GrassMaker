n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def turn_to_abs(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    
    print(*arr)

turn_to_abs(arr)
