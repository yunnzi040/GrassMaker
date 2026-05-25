def solution(a, b):
    answer = 0
    # a와 b가 같은 경우는 둘 중 아무 수나 리턴
    if a == b :
        return a
    
    n = max(a, b)
    m = min(a, b)
    
    for i in range(m, n+1):
        answer += i
    return answer