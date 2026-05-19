N = int(input())

arr = list(map(int, input().split(" ")))

# 2가 등장할 때마다 그때의 인덱스 저장
idx = 0 
count = 0

for i in range(len(arr)):
    if arr[i] == 2:
        count += 1
        idx = i
    
    if count == 3:
        print(idx+1)
        break
        


        