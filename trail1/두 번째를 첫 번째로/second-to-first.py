N = list(input())
a = N[1]
b = N[0]

for i in range(len(N)):
    if N[i] == a:
        N[i] = b

print("".join(N))

