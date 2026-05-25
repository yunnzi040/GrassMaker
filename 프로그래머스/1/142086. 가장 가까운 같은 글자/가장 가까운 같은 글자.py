def solution(s):
    answer = []    
    for i in range(len(s)):
        new_arr = s[:i] # b a n
        alpha = s[i] # a
        
        if alpha in new_arr:
            rev = new_arr[::-1]
            for j in range(len(rev)): # n a b
                if rev[j] == alpha:
                    answer.append(j + 1)
                    break
        else:
            answer.append(-1)
            
    return answer