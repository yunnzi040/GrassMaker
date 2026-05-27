def solution(number, limit, power):
    answer = 0
    count = [] # number까지의 약수를 담을 리스트
    
    for i in range(1, number+1):
        if i == 1:
            count.append(i)
        else:
            count.append(get_divisor_count(i))
            
    for j in count:
        if j > limit:
            j = power
        answer += j
    
    return answer


def get_divisor_count(n):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i == n:
                cnt += 1
            else:
                cnt += 2
    return cnt