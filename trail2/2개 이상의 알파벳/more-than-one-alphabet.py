A = input()

# Please write your code here.
def same_alphabet(n):
    cnt = 0
    for i in range(len(n)):
        for j in range(i, len(n)):
            if A[i] != A[j]:
                cnt += 1
            
            if cnt == 2 :
                return True
    return False


if same_alphabet(A):
    print("Yes")
else:
    print("No")
