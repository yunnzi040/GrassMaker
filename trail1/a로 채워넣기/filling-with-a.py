N = list(input())
for i in range(len(N)):
    if i == 1 or i == len(N)-2:
        N[i] = 'a'

print("".join(N))