n = int(input())

# Please write your code here.
def total(n):
    total = 0

    for i in range(n+1):
        total += i
    
    result = total // 10
    print(result)

total(n) 