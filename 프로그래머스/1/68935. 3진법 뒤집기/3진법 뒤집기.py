def solution(n):
    arr = []
    answer = 0
    
    # 앞뒤 반전(3진법) 구하기
    while n > 0:
        arr.append(n % 3)
        n //= 3

    for i in range(len(arr)):
        answer += (3 ** (len(arr) - 1 - i)) * arr[i] 
        
    return answer
