N, B = map(int, input().split())

# Please write your code here.
if N == 0:
    print(0)
else:
    result = []

    while N > 0:
        result.append(str(N % B))
        N //= B

    print("".join(reversed(result)))