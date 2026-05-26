a, b = map(int, input().split())
n = input()

# Please write your code here.
num = 0

# a진수로 표현된 어떤 수 N을 십진수로 표현
for i in range(len(n)):
    num = num * a + int(n[i])

# 십진수로 표현된 수를 다신 B진수로 표현
result = []
while num > 0:
    result.append(str(num % b))
    num //= b

print("".join(reversed(result)))
