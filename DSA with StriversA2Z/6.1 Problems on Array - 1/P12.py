def single_number(nums):
    res = 0
    for number in nums:
        res = res^number
    return res
nums = list(map(int,input().split()))
print(single_number(nums))