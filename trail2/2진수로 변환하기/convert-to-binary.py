n = int(input())

# Please write your code here.
result = []

if n == 0:
    print(0)
else:
    while n > 0:
        result.append(str(n % 2))
        n //= 2

print("".join(result[::-1]))