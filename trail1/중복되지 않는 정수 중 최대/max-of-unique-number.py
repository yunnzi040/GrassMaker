n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
result = [0 for _ in range(max(nums)+1)]
max = 0

for i in nums:
    result[i] += 1

for i in range(len(result)):
    if result[i] == 1 and max < i:
        max = i
    
if max == 0:
    print(-1)
else:
    print(max)



