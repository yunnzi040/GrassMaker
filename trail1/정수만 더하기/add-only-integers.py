s = input()
total = 0

for i in s:
    if i.isdigit():
        total += int(i)

print(total)
