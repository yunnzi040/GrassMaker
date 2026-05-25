def solution(n):
    # n의 양의 제곱근 구하기
    x = int(n ** 0.5)
    
    if x ** 2 == n: #n이 양의 정수 x의 제곱일 경우
        return (x+1) ** 2
    else:  #n이 양의 정수 x의 제곱이 아닐 경우
        return -1