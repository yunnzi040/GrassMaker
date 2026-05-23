N = int(input())

# Please write your code here.
def a(N):
    if N == 1:
        return 1
    total = N + a(N-1)
    return total

print(a(N))