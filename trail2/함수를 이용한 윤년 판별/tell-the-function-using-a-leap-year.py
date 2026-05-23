y = int(input())

# Please write your code here.
def leap_year(n):
    if n % 100 == 0 and n % 400 != 0:
        return "false"
    elif n % 4 != 0:
        return "false"
    return "true"  

print(leap_year(y))