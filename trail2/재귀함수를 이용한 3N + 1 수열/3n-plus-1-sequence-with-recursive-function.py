n = int(input())

# Please write your code here.
def calculate(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return calculate(n // 2) + 1
    elif n % 2 == 1:
        return calculate(3 * n + 1) + 1
    
print(calculate(n))
    
