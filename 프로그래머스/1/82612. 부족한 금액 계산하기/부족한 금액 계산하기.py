def solution(price, money, count):
    bill = 0 # 놀이기구의 이용금액
    
    for i in range(count+1):
        bill += (price * i)
    
    if money - bill > 0:
        return 0
    else :
        return abs(money - bill)
    