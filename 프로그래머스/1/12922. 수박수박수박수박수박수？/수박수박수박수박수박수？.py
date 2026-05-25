def solution(n):
    arr = ["수" if i % 2 == 0 else "박" for i in range(n) ]
    answer = "".join(arr)
    return answer