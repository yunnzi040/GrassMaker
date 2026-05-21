arr = list(map(int, input().split()))
up_500 = []
down_500 = []

for i in arr:
    if i > 500:
        up_500.append(i)
    elif i < 500:
        down_500.append(i)
    
print(max(down_500), min(up_500))

