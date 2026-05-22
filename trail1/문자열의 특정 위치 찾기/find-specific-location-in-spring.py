string, alpha = map(str, input().split())

index = string.find(alpha)

if index == -1:
    print("No")
else:
    print(index)