N = input()

# Please write your code here.
num = 0

# 십진수로 바꾸기
for i in range(len(N)):
    num = (num * 2) + int(N[i])

num *= 17

result = []
# 이진수로 나타내기
while num > 0:
    result.append(str(num % 2))
    num //= 2

print("".join(reversed(result)))

 