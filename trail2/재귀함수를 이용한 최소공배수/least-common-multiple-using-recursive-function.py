n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def gcd(a, b):
    # 최대공약수 재귀
    if b == 0:
        return a
    
    return gcd(b, a % b)


def lcm(a, b):
    # 최소공배수
    return (a * b) // gcd(a, b)


def find_lcm(arr, index):
    # 원소 하나만 남으면 자기 자신 반환
    if index == len(arr) - 1:
        return arr[index]

    # 현재 원소와 나머지 부분의 최소공배수 계산
    return lcm(arr[index], find_lcm(arr, index + 1))

print(find_lcm(arr, 0))
