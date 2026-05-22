n = int(input())
total = 0

for _ in range(n):
    num = int(input())
    total += num

str_total = list(str(total))
print("".join(str_total[1:] + [str_total[0]]))