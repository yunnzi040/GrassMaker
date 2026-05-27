def solution(k, m, score):
    score = sorted(score, reverse=True)
    answer = 0
    
    for i in range(len(score) // m):
        min_val = min(score[m * i : m * (i + 1)])
        answer += min_val * m 
        
    return answer