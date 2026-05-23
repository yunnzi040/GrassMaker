n = int(input())

# Please write your code here.
def calculate(n):
    if n == 0:
        return
    
    calculate(n-1)
    print("HelloWorld")

calculate(n)