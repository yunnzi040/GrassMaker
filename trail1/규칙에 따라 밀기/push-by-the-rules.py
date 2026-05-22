A = input()
LR = input()
arr = list(LR)
a_arr = list(A)

for i in arr:
    if i == 'R': #우측으로 한칸 밀기
        a_arr = [a_arr[-1]] + a_arr[:-1]
    else:
        a_arr = a_arr[1:]+ [a_arr[0]]

print("".join(a_arr))