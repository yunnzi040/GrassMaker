n = int(input())

# Please write your code here.
def reverse_a(N):
    if N == 0 :
        return
    
    reverse_a(N-1)
    print(N, end=" ")

def a(N):
    if N == 0:
        return

    print(N, end=" ")
    a(N-1)

reverse_a(n)
print()
a(n)


