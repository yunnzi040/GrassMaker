def solution(array, commands):
    answer = []
        
    for c in commands:
        i = c[0]
        j = c[1]
        k = c[2]
                
        new_arr = sorted(array[i-1:j])
        answer.append(new_arr[k-1])
        new_arr = []
        
    return answer