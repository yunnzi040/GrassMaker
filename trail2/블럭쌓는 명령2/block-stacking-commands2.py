n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
arr_n = [0 for i in range(n)]

for i in commands: # (7, 4), (5, 5) ...
    start, end = int(min(i)), int(max(i))
    for j in range(start-1, end):
        arr_n[j] += 1
    
        
print(max(arr_n))
        
