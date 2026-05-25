def solution(n):
    answer = []
    for _ in range(len(str(n))):
        answer.append(n%10)
        n//=10
    answer = sorted(answer, reverse=True)
    number = int("".join(map(str, answer)))
    
    return number