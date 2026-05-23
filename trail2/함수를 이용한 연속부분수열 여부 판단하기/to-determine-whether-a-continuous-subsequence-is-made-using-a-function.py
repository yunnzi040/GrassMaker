n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
# 연속부분수열인지 확인하는 함수
def consecutive(word):
    for i in range(len(word)):
        if word[i] != b[i]:
            return False
    return True

result = "No"

for i in range(n1-n2+1):
    # 연속부분수열인지 확인
    word = a[i:i+n2]

    if consecutive(word):
        result = "Yes"
        break

print(result)
