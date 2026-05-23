N = int(input())

# Please write your code here.
def output(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2

    if N % 2 == 0:
        return N + output(N-2)
    elif N % 2 == 1:
        return N + output(N-2)
    
print(output(N))
