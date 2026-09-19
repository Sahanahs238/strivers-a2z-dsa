import math
def sumbyD(nums,div):
    Sum =0
    for num in nums:
        Sum += math.ceil(num/div)
    return Sum
def smallestDivisor(nums,limit):
    if len(nums)>limit:
        return -1
    low =1
    high = max(nums)
    ans =-1
    while low<= high:
        mid=(low+high)//2
        if sumbyD(nums,mid)<=limit:
            ans = mid
            high=mid-1
        else:
            low = mid +1
    return ans
nums = [1, 2, 3, 4, 5]
limit = 8
print(smallestDivisor(nums,limit))

