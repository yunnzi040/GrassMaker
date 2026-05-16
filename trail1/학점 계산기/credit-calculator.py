N = int(input())
scores = list(map(float, input().split()))

avg = round(sum(scores)/N, 1) 
print(f"{avg:.1f}")

if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")
