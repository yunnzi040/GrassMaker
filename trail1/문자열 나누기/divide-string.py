N = int(input())
arr = list(map(str, input().split()))
string = "".join(arr)

for i in range(len(string)):
    if i % 5 == 4:
        print(string[i], end="")
        print()
        continue
    print(string[i], end="")
