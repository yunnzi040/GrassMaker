n = int(input())

# Please write your code here.
def find(a, b):
    return n % 2 == 0 and (a + b) % 5 == 0

ten_count = n // 10
one_count = n % 10

if find(ten_count, one_count):
    print("Yes")
else :
    print("No")