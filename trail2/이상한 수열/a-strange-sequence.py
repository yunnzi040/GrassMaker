N = int(input())

# Please write your code here.
def calculate(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    return calculate(n//3) + calculate(n-1)

print(calculate(N))