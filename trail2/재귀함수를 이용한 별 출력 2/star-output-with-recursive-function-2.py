n = int(input())

# Please write your code here.
def calculate(N):
    if N == 0 :
        return "*"
    
    print("* " * N)
    calculate(N-1)
    print("* " * N)

calculate(n)