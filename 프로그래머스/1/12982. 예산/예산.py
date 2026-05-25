def solution(d, budget):
    d = sorted(d) 
    
    for i in range(len(d), -1, -1):
        total = sum(d[:i])
        
        if budget >= total:
            return i    
