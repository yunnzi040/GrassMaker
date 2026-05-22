arr = list(map(str, input().split()))
total = 0
for word in arr:
    for w in word:
        total += 1

print(total)