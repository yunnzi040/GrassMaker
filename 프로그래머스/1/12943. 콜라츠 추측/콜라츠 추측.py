def solution(num):
    cnt = 0
    
    # 어진 수가 1인 경우에는 0 리턴
    if num == 1:
        return 0
    
    while num != 1:
        if num % 2 == 0:
            num //= 2
            cnt += 1
            
        elif num % 2 == 1:
            num = 3 * num + 1
            cnt += 1
            
        # 500번 반복할 때까지 1이 되지 않는다면 –1을 반환
        if cnt == 500 and num != 1:
            return -1
            

    return cnt