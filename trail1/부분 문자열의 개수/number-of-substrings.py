A = input()
B = input()

cnt=0

for i in range(len(A)-1):
    word = A[i]+A[i+1]
    if word == B:
        cnt += 1

print(cnt)
