n, k = map(int, input().split())

# Please write your code here.
from collections import deque

d = deque(range(1, n + 1))
answer = []

while d:
    # 앞 원소를 뒤로 보내기 k-1번
    for _ in range(k - 1):
        d.append(d.popleft())

    # k번째 원소 제거
    answer.append(d.popleft())

print(*answer)
