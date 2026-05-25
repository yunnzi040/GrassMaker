n = int(input())
sequence = list(map(int, input().split()))

class Where_index:
    def __init__(self, num, input_n):
        self.num = num
        self.input_n = input_n

numbers = [Where_index(sequence[i], i) for i in range(n)]

numbers.sort(key=lambda x: (x.num, x.input_n))

result = [0] * n

for i in range(len(numbers)):
    original_index = numbers[i].input_n
    result[original_index] = i + 1

for r in result:
    print(r, end=" ")