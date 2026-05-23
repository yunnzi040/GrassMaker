M, D = map(int, input().split())

# Please write your code here.
# 7보다 작은 홀수 달은 31일까지 있음
# 7보다 큰 짝수 달은 31일까지 있음

def this_date_exist(M, D):
    if M == 2:
        return D <= 28
    elif M <= 7: 
        if M % 2 != 0 and D <= 31: # 1, 3, 5, 7월은 31일까지 있음
            return True
        elif M % 2 == 0 and D <= 30: # 4, 6월은 30일까지 있음
            return True
    elif M <= 12:
        if M % 2 == 0 and D <= 31: # 8, 10, 12월은 31일까지 있음
            return True
        elif M % 2 != 0 and D <= 30: # 9, 11월은 30일까지 있음
            return True
    return False


if this_date_exist(M, D):
    print("Yes")
else :
    print("No")
    
