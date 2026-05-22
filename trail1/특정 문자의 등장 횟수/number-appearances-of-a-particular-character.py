string = input()
eb_cnt = 0
ee_cnt = 0

for i in range(len(string)-1):
    word = string[i] + string[i+1]
    if word == 'ee':
        ee_cnt += 1
    
    if word == 'eb':
        eb_cnt += 1
    
print(ee_cnt, eb_cnt)
        