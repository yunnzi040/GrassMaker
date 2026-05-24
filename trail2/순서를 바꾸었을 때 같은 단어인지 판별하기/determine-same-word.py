word1 = input()
word2 = input()

# Please write your code here.
def is_same(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)

    if s1 == s2:
        return True
    else:
        return False

if is_same(word1, word2):
    print("Yes")
else:
    print("No")
