a, b, c = map(int, input().split())

# Please write your code here.
def calculate(n):
    if n < 10:
        return n
    
    return (calculate(n // 10) + (n % 10))

print(calculate(a*b*c))

