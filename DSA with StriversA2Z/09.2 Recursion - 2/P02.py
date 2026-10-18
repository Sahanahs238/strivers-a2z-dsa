def countSubsequenceK(nums,k):
    subset =[]
    count = 0
    def backtrack(i):
        nonlocal count
        if i ==len(nums):
            if sum(subset)==k:
                count+=1
            return 
        subset.append(nums[i])
        backtrack(i+1)
        subset.pop()
        backtrack(i+1)
    backtrack(0)
    return count
nums = [4, 9, 2, 5, 1]
k = 10
print(countSubsequenceK(nums,k))