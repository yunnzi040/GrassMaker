def solution(cards1, cards2, goal):
    answer = []
    idx1 = 0
    idx2 = 0
    vaild = True    
    
    for i in range(len(goal)):
        if idx1 < len(cards1) and goal[i] == cards1[idx1]:
            idx1 += 1
        elif idx2 < len(cards2) and goal[i] == cards2[idx2]:
            idx2 += 1
        else:
            vaild = False
            break

    if vaild:
        return "Yes"
    else:
        return "No"