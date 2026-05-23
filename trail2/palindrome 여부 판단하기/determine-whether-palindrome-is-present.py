A = input()

# Please write your code here.
def palindrome(s):
    if A == s[::-1]:
        return True
    else :
        return False

if palindrome(A):
    print("Yes")
else :
    print("No")