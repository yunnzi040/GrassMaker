n = input()
arr = list(n)

index = n.find("e")
new_arr = arr[:index] + arr[index+1:]
print("".join(new_arr))

