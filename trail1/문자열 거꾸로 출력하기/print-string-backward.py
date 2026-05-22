for _ in range(10):
    str = []
    word = input()

    if word == 'END':
        break

    for i in range(len(word)-1, -1, -1):
        str.append(word[i])

    print("".join(str))