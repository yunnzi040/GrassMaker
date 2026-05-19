arr = list(map(int, input().split()))
count_arr = [ 0 for _ in range(10)]
for a in arr:
    if a == 0:
        break    
    ten = int(a/10)
    count_arr[ten-1] += 1

for i in range(9):
    print(str(i+1) + " - " + str(count_arr[i]))

