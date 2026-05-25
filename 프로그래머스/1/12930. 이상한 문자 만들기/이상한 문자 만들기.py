def solution(s):
    arr = s.split(" ")
    result = []
    
    for i in range(len(arr)):
        words = ""
        for j in range(len(arr[i])):
            if j % 2 == 0:
                words += arr[i][j].upper()
            elif j % 2 == 1:
                words += arr[i][j].lower()
                
        result.append(words)
                
    return " ".join(result)