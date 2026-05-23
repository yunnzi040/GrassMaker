text = input()
pattern = input()

# Please write your code here.
# text에서 patten 문자열이  부분 문자열로 존재하는 경우 시작 인덱스

def find_part_index():
    return text.find(pattern)

print(find_part_index())