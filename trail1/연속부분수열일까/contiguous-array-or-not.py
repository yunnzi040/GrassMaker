N1, N2 = map(int, input().split()) # 수열 A, B의 원소의 개수

# 수열 A를 입력 받습니다.
A = list(map(str, input().split()))

# 수열 B를 입력 받습니다. 
B = list(map(str, input().split()))


for i in range(len(A)):
    compare = A[i:i+len(B)]
    if compare == B:
        vaild = "Yes"
        break
    else:
        vaild = "No"

print(vaild)


