def solution(x):
    answer = True
    num = x
    total = 0
    
    # x의 자릿수의 합 구하기
    for _ in range(len(str(num))):
        total += num % 10
        num //= 10
        
    if x % total != 0:
        answer = False
        
    return answer