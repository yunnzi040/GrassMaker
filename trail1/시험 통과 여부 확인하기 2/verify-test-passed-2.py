N = int(input())
pass_count = 0

for _ in range (N):
    scores = list(map(int, input().split()))
    avg = round(sum(scores)/4, 2)

    if avg >= 60:
        print("pass")
        pass_count += 1
    else:
        print("fail")

print(pass_count)