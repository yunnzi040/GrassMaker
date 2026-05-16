arr = list(map(int, input().split()))
stack = [] 

for n in arr:
    if n == 0: # 0을 만났다면 입력 중지
        break
    else: # 0을 만나지 않으면 리스트에 추가
        stack.append(n)

for i in range(len(stack)-1, -1, -1):
    print(stack[i], end=" ")

