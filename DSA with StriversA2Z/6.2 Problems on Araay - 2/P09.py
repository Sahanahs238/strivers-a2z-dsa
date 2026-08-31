def leaders(nums):
    n = len(nums)
    max_leader = nums[n-1]
    ans =[]
    ans.append(max_leader)
    for i in range(n-2,-1,-1):
        if nums[i]>max_leader:
            ans.append(nums[i])
            max_leader = nums[i]
    ans.reverse()
    return ans
nums = list(map(int,input().split()))
print(leaders(nums))