result = []
cnt = 0

while True:
    s = input()

    if s == '0':
        break

    if cnt % 2 == 0:
        result.append(s)

    cnt += 1

print(cnt)
print("\n".join(result))