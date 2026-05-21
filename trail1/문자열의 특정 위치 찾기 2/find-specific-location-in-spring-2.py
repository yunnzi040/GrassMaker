words = [ "apple", "banana", "grape", "blueberry", "orange"]

alpha = input()
total = 0

for i in words:
    if alpha == i[2] or alpha == i[3]:
        print(i)
        total += 1

print(total)