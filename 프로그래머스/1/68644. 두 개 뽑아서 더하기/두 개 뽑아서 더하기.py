def solution(numbers):
    answer = []
    
    for i in range(len(numbers)): # 0 ~ 4
        for j in range(i+1, len(numbers)): # 1 ~ 4
            sum = numbers[i] + numbers[j]
            if sum not in answer:
                answer.append(sum)
    answer = sorted(answer)
    return answer