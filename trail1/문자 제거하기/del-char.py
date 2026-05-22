
N = input()
arr = list(N)

while len(arr) > 1:
    num = int(input())

    # 주어진 정수가 문자열의 길이 이상이면 마지막 문자를 제거
    if num >= len(arr):
        arr.pop(-1)
    else:
        arr.pop(num)

    print("".join(arr))