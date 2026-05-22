a = input()
arr = list(a)
b = input()
cnt = 1


while True:
    arr = [arr[-1]] + arr[:-1]
    str_a = "".join(arr)
    
    if str_a == b:
        print(cnt)
        break

    if cnt > 1 and str_a == a:
        print(-1)
        break
    
    cnt += 1

