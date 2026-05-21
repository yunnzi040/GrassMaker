a, b = input().split()
if len(a)>len(b):
    print(a, str(len(a)))
elif len(a)<len(b):
    print(b, str(len(b)))
else:
    print("same")
    