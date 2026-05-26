def solution(strings, n):
    answer = []
    answer = sorted(strings, key=lambda x: (x[int(n)], x))
            
    return answer