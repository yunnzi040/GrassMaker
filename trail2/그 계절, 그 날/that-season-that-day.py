Y, M, D = map(int, input().split())

# Please write your code here.
# Y가 윤년인지 확인하는 함수
def leap_year(Y):
    if Y % 400 == 0:
        return True
    elif Y % 100 == 0:
        return False
    elif Y % 4 == 0:
        return True
    else:
        return False

# Y해에 M월 D일이 존재하는지 확인하는 함수
def date_exist_in_year(leap_exist, M, D):
    if M == 2:
        if leap_exist == True: # 윤년일 경우
            return D <= 29
        else : # 윤년이 아닐 경우
            return D <= 28

    elif M <= 7:
        if M % 2 != 0 and D <= 31:
            return True
        elif M % 2 == 0 and D <= 30:
            return True

    elif M <= 12:
        if M % 2 == 0 and D <= 31:
            return True
        elif M % 2 != 0 and D <= 30:
            return True
    return False

def seasons(M):
    if M >= 3 and M <= 5:
        return "Spring"
    elif M >= 6 and M <= 8:
        return "Summer"
    elif M >= 9 and M <= 11:
        return "Fall"
    else:
        return "Winter"

if date_exist_in_year(leap_year(Y), M, D):
    print(seasons(M))
else:
    print(-1)