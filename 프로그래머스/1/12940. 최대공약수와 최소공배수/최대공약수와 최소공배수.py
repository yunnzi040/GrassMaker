def solution(n, m):
    answer = [0] * 2
    
    # 최대공약수 구하기
    for i in range(min(n, m)+1, -1, -1):
        if n % i == 0 and m % i == 0:
            answer[0] = i
            break
            
    # 최소공배수 구하기
    answer[1] = n * m // answer[0]
            
    
    return answer