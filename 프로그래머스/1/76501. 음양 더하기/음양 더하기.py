def solution(absolutes, signs):
    
    for i in range(len(absolutes)):
        if signs[i]: # 양수
            continue
        else:
            absolutes[i] = 0 - absolutes[i]
    
    return sum(absolutes)