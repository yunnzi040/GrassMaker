n = input()
L = len(n)
arr = list(n)


for i in range(L+1):
    if i == 0 :
        print("".join(arr))
    else:
        arr = [arr[-1]] + arr[:L-1]
        print("".join(arr))
    