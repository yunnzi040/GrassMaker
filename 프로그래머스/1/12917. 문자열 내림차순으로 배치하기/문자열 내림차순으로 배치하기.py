def solution(s):
    words = list(s)
    words = sorted(words)
    answer = "".join(words[::-1])
    return answer