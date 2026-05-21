n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
min_val = price[0]
max_profit = 0

for i in price:
    if min_val > i: # 최소 가격 갱신
        min_val = i
    
    if max_profit < i - min_val:
        max_profit = i - min_val
    
    
print(max_profit)
    
