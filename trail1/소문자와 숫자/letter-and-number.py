s = input()
result = []

for i in s:
    if i.isalpha():
        result.append(i.lower())
    elif i.isdigit():
        result.append(i)

print("".join(result))
