def solution(arr):
    answer = []
    
    if len(arr) == 1:
        return [-1]
    
    min_val = arr[0]
    index = 0
    
    for i in range(len(arr)):
        if min_val > arr[i]:
            min_val = arr[i]
            index = i
    
    arr.pop(index)
    
    return arr