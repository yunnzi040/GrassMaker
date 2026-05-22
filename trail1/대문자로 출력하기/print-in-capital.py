string = input()
result = []

for i in string:
    if i.isalpha():
        result.append(i.upper())

print("".join(result))