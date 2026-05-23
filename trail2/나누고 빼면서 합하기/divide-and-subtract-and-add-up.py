n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def calculate(n, m):
    cnt = 0

    while m > 0:
        if m % 2 == 1:
            cnt += A[m-1]
            m -= 1
        else :
            cnt += A[m-1]
            m //=2

    return cnt

print(calculate(n, m))

        