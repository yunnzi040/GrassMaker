N, Q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range (Q):
    q_arr = list(map(int, input().split()))
    q_first = q_arr[0]
    q_number = q_arr[1:]

    if q_first == 1: # 1 a 일 경우
        print(arr[q_number[0]-1])
    elif q_first == 2: # 2 b 일 경우
        if q_number[0] not in arr:
            print("0")
        else:
            print(arr.index(q_number[0])+1)

    else: # 3 s e 일 경우
        print(*arr[q_number[0]-1:q_number[1]])