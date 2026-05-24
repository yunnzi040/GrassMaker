n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def find_max(arr, index):
    # 종료
    if index == len(arr)-1:
        return arr[index]
    
    return max(arr[index], find_max(arr, index+1))

print(find_max(arr, 0))