def singleNumber2(nums):
    ones = 0
    twos = 0
    for num in nums :
        ones = (ones^num)&~twos
        twos = (twos^num)&~ones
    return ones
nums = [2,2,2,3]
print(singleNumber2(nums))