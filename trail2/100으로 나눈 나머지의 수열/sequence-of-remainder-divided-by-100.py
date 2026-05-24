N = int(input())

# Please write your code here.
def calculate(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    
    return (calculate(n-2) * calculate(n-1)) % 100

print(calculate(N))
