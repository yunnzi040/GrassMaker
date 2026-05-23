N = int(input())

# Please write your code here.
def a(N):
    if N < 10:
        return N ** 2
    
    return (N % 10) ** 2 + a(N // 10)

print(a(N))