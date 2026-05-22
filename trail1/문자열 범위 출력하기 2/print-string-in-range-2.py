string = input()
N = int(input())

if N > len(string):
    for i in range(len(string)-1, -1, -1):
        print(string[i], end="")
else:
    for i in range(len(string)-1, len(string)-1-N, -1):
        print(string[i], end="")