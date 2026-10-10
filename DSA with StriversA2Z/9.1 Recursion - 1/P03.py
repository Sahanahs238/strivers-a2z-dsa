def subset(nums):
    subset = []
    res =[]
    def backtrack(i):
        if i==len(nums):
            res.append(subset.copy())
            return 
        subset.append(nums[i])
        backtrack(i+1)
        subset.pop()
        backtrack(i+1)
    backtrack(0)
    return res 
nums = [1,2,3]
print(subset(nums))
