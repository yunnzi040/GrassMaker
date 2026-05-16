scores = list(map(float, input().split()))

avg = round(sum(scores)/8, 1)
print(f"{avg:.1f}")