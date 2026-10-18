def fourSum(nums,target):
    res = []
    nums.sort()
    for i in range(len(nums)):
        if i!=0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,len(nums)):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            l = j+1
            r =len(nums)-1
            while l<r:
                total = nums[i]+nums[j]+nums[l]+nums[r]
                if total > target :
                    r -= 1
                elif total < target:
                    l+=1
                else:
                    res.append([nums[i],nums[j],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
    return res
nums = list(map(int,input().split()))
target = int(input("target:"))
print(fourSum(nums,target))