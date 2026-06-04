n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
a = []
b = []

def position(dir, time):
    pos = 0
    pos_arr = []

    for i in range(len(dir)):
        if dir[i] == 'R':
            for j in range(time[i]):
                pos += 1
                pos_arr.append(pos)
        else:
            for j in range(time[i]):
                pos -= 1
                pos_arr.append(pos)
    
    return pos_arr

a_arr = position(d, t)
b_arr = position(d2, t2)

vaild = False
index = 0

for i in range(max(len(a_arr), len(b_arr))):
    if a_arr[i] == b_arr[i]:
        index = i + 1
        vaild = True
        break

if vaild:
    print(index)
else:
    print(-1)
    

