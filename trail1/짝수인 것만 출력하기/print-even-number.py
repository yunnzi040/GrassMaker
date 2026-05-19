N = int(input())
arr = list(map(int, input().split(" ")))
even = [n for n in arr if n % 2 == 0]
print(*even)