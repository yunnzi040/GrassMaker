nums = list(map(int, input().split()))
sum = 0
count = 0

for i in nums:
    if i < 250:
        sum += i
        count += 1
    else :
        break

avg = sum / count

print(str(sum) + " " + f"{avg:.1f}")
