def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        line = arr1[i] | arr2[i]
        binary = bin(line)[2:].zfill(n)
        result = binary.replace("1", "#").replace("0"," ")
        answer.append(result)
    return answer
        
        
        
        
        