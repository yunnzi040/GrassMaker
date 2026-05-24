n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class Person:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

persons = [Person(name[i], street_address[i], region[i]) for i in range(n)]

name = sorted(name)

for i in persons:
    if i.name == name[n-1]:
        print(f"name {i.name}")
        print(f"addr {i.address}")
        print(f"city {i.region}")
        break


