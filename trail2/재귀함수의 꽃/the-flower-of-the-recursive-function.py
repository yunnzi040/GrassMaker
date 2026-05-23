N = int(input())

# Please write your code here.
def calculate(N):
    if N == 0:
        return
    
    print(N, end=" ")
    calculate(N-1)
    print(N, end=" ")

calculate(N)
