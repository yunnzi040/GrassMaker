def solution(name, yearning, photo):
    answer = []
    
    for i in photo:
        score = 0
        for j in range(len(i)):            
            if i[j] in name:
                idx = name.index(i[j])
                score += yearning[idx]
        answer.append(score)
        
    return answer