def singleNumber(nums):
    xor = 0
    for i in range(len(nums)):
        xor ^= nums[i]
    return xor
nums = [1, 2, 2, 4, 3, 1, 4]
print(singleNumber(nums))