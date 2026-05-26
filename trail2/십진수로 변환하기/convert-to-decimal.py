binary = input()

# Please write your code here.
total = 0

for i in range(len(binary)):
    total = total * 2 + int(binary[i])

print(total)