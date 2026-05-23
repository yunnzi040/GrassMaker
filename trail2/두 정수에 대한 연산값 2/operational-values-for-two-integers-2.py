a, b = map(int, input().split())

# Please write your code here.
def calculate(n, m):
    if max(n, m) == n :
        return n * 2, m + 10
    else :
        return n + 10, m * 2

print(*calculate(a, b))