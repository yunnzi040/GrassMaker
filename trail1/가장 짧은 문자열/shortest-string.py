import sys
min_len = sys.maxsize
max_len = 0

for _ in range(3):
    word = input()

    if min_len > len(word):
        min_len = len(word)
    
    if max_len < len(word):
        max_len = len(word)

print(max_len - min_len)
