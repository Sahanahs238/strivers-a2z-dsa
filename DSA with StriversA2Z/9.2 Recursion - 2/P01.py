def subsetK(nums,k):
    subsets=[]
    def backtrack(i):
        if i ==len(nums):
            return sum(subsets)==k
        subsets.append(nums[i])
        if backtrack(i+1):
            return True
        subsets.pop()
        if backtrack(i+1):
            return True 
        return False
    return backtrack(0)
nums = [1, 2, 3, 4, 5]
k = 8
print(subsetK(nums,k))
