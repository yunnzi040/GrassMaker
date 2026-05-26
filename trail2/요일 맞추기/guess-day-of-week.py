m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def get_days(m, d):
    return sum(num_of_days[:m]) + d

diff = get_days(m2, d2) - get_days(m1, d1)

print(weeks[diff % 7])