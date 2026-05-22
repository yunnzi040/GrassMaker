A = input()
B = input()

# Please write your code here.
for _ in range(len(A)):
    # 가장 앞에 등장하는 B의 인덱스 구하기
    index = A.find(B)

    # 남은 문자열에서 B와 일치하는 문자열이 존재하지 않을 경우 반복문 종료 후 남은 문자열 출력
    if index == -1:
        print("".join(A))
        break

    arr = list(A)
    arr = arr[:index] + arr[index+len(B):]
    A = "".join(arr)
