N = int(input())
arr = list(map(int, input().split(" ")))
count = [0 for _ in range (9)]

for i in arr:
    count[i-1] += 1

print(*count, sep="\n")

