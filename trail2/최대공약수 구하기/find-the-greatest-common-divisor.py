n, m = map(int, input().split())

# Please write your code here.
def GCD(n, m):
    gcd = 1
    for i in range(1, min(n, m)+1):
        if n % i == 0 and m % i == 0 and gcd < i:
            gcd = i
    
    print(gcd)

GCD(n,m)
    
