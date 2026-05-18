arr = list(map(int, input().split(" ")))

even_sum = sum(arr[1::2])
three_avg = round(sum(arr[2::3])/len(arr[2::3]), 1)

print(str(even_sum) + " " + f"{three_avg:.1f}")