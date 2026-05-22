input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Please write your code here.
arr = list(input_str)

for i in queries :
    if i == 1:
        arr = arr[1:] + [arr[0]]
        print("".join(arr))

    elif i == 2:
        arr = [arr[-1]] + arr[:len(arr)-1]
        print("".join(arr))

    else:
        arr = arr[::-1]
        print("".join(arr))



