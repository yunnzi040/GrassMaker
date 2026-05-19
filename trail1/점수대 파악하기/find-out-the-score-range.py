arr = list(map(int, input().split()))
count = [ 0 for _ in range(10)]
i = 100

for a in arr:
    if a == 0:
        break
    if a // 10 == 0:
        continue
    score = a // 10
    count[score-1] += 1

for a in range(len(count)-1, -1, -1): # -9, -8, -7
    print(str(i) + " - " + str(count[a]))
    i -= 10

    
    