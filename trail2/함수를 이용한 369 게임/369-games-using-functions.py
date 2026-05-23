a, b = map(int, input().split())

# Please write your code here.
def three_six_nine(n):
    return '3' in str(n) or '6'in str(n) or '9' in str(n)

def three_multi(n):
    if n % 3 == 0:
        return True
    else:
        return False

cnt = 0

for i in range(a, b+1):
    if three_six_nine(i): #3, 6, 9 중에 하나가 들어가 있는지 확인
        cnt += 1
    elif three_multi(i): # 수 자체가 3의 배수인 수인지 확인
        cnt += 1

print(cnt)