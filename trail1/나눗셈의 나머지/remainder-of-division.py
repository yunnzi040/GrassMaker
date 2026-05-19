A, B = map(int, input().split())

remains = [0 for _ in range(B)]
total = 0

while A > 1:
    rm = A % B
    remains[rm] += 1

    A = A // B

for i in range(len(remains)):
    total += remains[i] * remains[i]

print(total)