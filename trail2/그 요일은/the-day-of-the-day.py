m1, d1, m2, d2 = map(int, input().split()) 
A = input() 
# Please write your code here. 
cnt = 0 # A 요일이 등장하는 횟수 
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 

def get_days(m, d): 
    return sum(num_of_days[:m]) + d 
    

diff = get_days(m2, d2) - get_days(m1, d1) + 1
cnt = diff // 7 

if A in weeks[:diff % 7]: 
    cnt += 1
    
print(cnt)