n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_val = a[0] # 초기 최솟값을 0번째 값으로 지정. 탐색 범위 1번째 인덱스부터
count = 0 # 최솟값의 개수세기

for i in a[1:]:
    if min_val > i:
        min_val = i

for i in a:
    if i == min_val:
        count += 1
    
print(str(min_val) + " " + str(count))