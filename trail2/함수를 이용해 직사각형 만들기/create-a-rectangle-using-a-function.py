n, m = map(int, input().split())

# Please write your code here.
def print_star_rectangle(row, col):
    for _ in range(row):
        for _ in range(col):
            print("1", end="")
        print()
    
print_star_rectangle(n, m)