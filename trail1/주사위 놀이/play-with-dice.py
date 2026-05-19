arr = list(map(int, input().split()))
count = [0 for _ in range(6)]

for a in arr:
    count[a-1] += 1

for i in range(len(count)):
    print(str(i+1) + " - " + str(count[i]))
