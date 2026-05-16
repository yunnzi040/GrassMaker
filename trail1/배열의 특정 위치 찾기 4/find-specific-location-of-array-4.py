nums = list(map(int, input().split()))
arr = []

for n in nums:
    if n == 0:
        break
    elif n!= 0 and n % 2 == 0:
        arr.append(n)

print(str(len(arr)) + " " + str(sum(arr)))

