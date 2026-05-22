s = input()
result = []

for i in s:
    i_int = ord(i)

    # 대문자일 경우
    if i_int >= ord('A') and i_int <= ord('Z'):
        result.append(i.lower())
    else:
        result.append(i.upper())

print("".join(result))
