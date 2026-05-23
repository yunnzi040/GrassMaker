a, b = map(int, input().split())

# Please write your code here.
def calculate(n, m):
    if max(n, m) == n :
        return n + 25, m * 2
    else :
        return n * 2, m + 25

print(*calculate(a, b))