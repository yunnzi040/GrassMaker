S, Q = map(str, input().split())
S_arr = list(S)

for _ in range(int(Q)):
    arr = list(input().split())

    # 1 a b
    if arr[0] == '1':
        a = int(arr[1])-1
        b = int(arr[2])-1

        str = S_arr[a]
        S_arr[a] = S_arr[b]
        S_arr[b] = str


    else: # 2 x y
        for i in range(len(S_arr)):
            if S_arr[i] == arr[1]:
                S_arr[i] = arr[2]

    print("".join(S_arr))





