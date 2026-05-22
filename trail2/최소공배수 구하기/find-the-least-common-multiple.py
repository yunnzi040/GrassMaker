n, m = map(int, input().split())

# Please write your code here.
def LCM(n, m):
    multi = 1
    
    while True:
        if (n * multi) % m == 0:
            print(n * multi)
            break
        
        multi += 1

LCM(n, m) 