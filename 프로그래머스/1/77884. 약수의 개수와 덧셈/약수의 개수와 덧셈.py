def solution(left, right):
    answer = 0 
    
    
    for i in range(left, right + 1):
        cnt = 0 # 약수의 갯수

        # i의 약수 구하기
        for j in range(1, i+1): # 1부터 i까지
            if i % j == 0:
                cnt += 1
                          
        if cnt % 2 == 0:
            answer += i
        elif cnt % 2 == 1:
            answer -= i
        
        
    return answer