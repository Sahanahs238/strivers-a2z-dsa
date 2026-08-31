def maxsubarray(nums):
    maxsub = nums[0]
    cursum = 0
    for n in nums:
        if cursum < 0:
            cursum = 0
        cursum += n
        maxsub=max(maxsub,cursum)
    return maxsub
nums = list(map(int,input().split()))
print(maxsubarray(nums))