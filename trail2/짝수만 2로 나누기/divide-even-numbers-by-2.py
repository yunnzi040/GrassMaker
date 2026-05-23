n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
new_arr = []

def divide(arr):
    for i in arr:
        if i % 2 == 0:
            new_arr.append(i // 2)
        else :
            new_arr.append(i)
    print(*new_arr, end=" ")

divide(arr)
