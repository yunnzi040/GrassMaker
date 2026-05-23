a, b = map(int, input().split())

# Please write your code here.
total = 0

def prime_number(i):
    if i == 1:
        return False 

    for a in range(2, i):
        if i % a == 0: # 소수가 아닐 때
            return False

    return True

for i in range(a, b+1):
    if prime_number(i): # 소수일 때
        total += i

print(total)

