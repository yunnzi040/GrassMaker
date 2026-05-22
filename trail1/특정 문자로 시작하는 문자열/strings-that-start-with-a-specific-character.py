N = int(input())
arr = [input() for _ in range(N)]
alpha = input()

result = []
total = 0

for a in arr:
    if a[0] == alpha:
        result.append(a)
        total += len(a)

avg = round(total/len(result), 2)

print(len(result), f"{avg:.2f}")





    
