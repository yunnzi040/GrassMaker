A = input()

# Please write your code here.
def same_alphabet(n):
    for i in range(len(n)):
        if A[i] != A[0]:
            return True
    return False


if same_alphabet(A):
    print("Yes")
else:
    print("No")
