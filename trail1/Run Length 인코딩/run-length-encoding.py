A = input()

# Please write your code here.
cnt = 1
word = A[0]
result = ""


for i in range(len(A)-1):
    if A[i+1] == word:
        cnt += 1

    else:
        result += (word + str(cnt))
        word = A[i+1]
        cnt = 1
    
result += (word + str(cnt))

print(len(result))
print(result)
        


    