n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
def calculate(nums):
    nums = sorted(nums)
    result = 0
    for i in range(len(nums)):
        max_val = nums[i] + nums[-1-i]

        if max_val > result:
            result = max_val

    return result

print(calculate(nums))