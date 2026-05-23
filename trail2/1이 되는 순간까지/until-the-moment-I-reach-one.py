N = int(input())

# Please write your code here.
cnt = 0
def a(n):
    global cnt 
    if n == 1:
        return cnt

    if n % 2 == 0:
        cnt += 1
        return a(n // 2)
    elif n % 2 == 1:
        cnt += 1
        return a(n // 3)

print(a(N))