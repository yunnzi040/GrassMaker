n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def calculate(a, b):
    global arr
    total = 0
    for i in range(a-1, b):
        total += arr[i]
    print(total)


for i in queries: 
    calculate(i[0], i[1])
