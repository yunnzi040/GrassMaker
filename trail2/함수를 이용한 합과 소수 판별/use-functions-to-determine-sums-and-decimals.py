a, b = map(int, input().split())

# Please write your code here.

# 소수 찾는 함수
def find_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 모든 자릿수의 합이 짝수인지 확인하는 함수
def cnt_is_even(n):
    string = str(n)
    cnt = 0

    for i in string:
        cnt += int(i)

    if cnt % 2 == 0:
        return True
    
    return False

total = 0

for i in range(a, b+1):
    if find_prime(i) and cnt_is_even(i):
        total += 1

print(total)
