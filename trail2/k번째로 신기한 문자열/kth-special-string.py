n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
def print_k_index(str, k):
    str = sorted(str)
    result = []
    for i in str:
        if i[:len(t)] == t:
            result.append(i)
    return result[k-1]

print((print_k_index(str, k)))

