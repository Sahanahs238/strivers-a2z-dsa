def subsetSum(nums):
    res =[]
    def backtrack(i,total):
        if i == len(nums):
            res.append(total)
            return
        backtrack(i+1,total+nums[i])
        backtrack(i+1,total)
    backtrack(0,0)
    return res
nums =[2, 3]
print(subsetSum(nums))