N, M = map(int, input().split())
arr = list(map(int, input().split()))

# M이 몇 번 등장하는지 구해 출력하기
cnt = arr.count(M)
print(cnt)
