arr = [0 for _ in range(10)]
result = []

for i in range(10):
    fruit = input()
    arr[i]=fruit

alpha = input()

for i in arr:
    if i[-1] == alpha:
        result.append(i)

if result:
    for i in result:
        print(i)
else:
    print("None")
