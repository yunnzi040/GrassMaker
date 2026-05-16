arr = []
numbers = list(map(int, input().split()))

for n in numbers:
    if n == 0:
        break
    else:
        arr.append(n)

sum = sum(arr)
avg = round(sum/len(arr), 1)

print(str(sum) + " " + f"{avg:.1f}")
