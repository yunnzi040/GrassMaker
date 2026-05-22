N = int(input())
total = 0
a_count = 0

for _ in range(N):
    word = input()
    if word[0] == 'a':
        a_count += 1
    total += len(word)


print(total, a_count)
