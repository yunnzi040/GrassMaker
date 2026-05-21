arr = list(map(int, input().split()))
min_val = max_val = arr[0]

for a in arr:
    if a == 999 or a == -999: #999 or -999일 경우 반복문 종료
        break
    
    if min_val > a:
        min_val = a

    if max_val < a:
        max_val = a

print(max_val, min_val)