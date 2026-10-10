def combinationSum(candidates,target):
    subset =[]
    res=[]
    def backtrack(i,total):
        if total == target:
            res.append(subset.copy())
            return
        if i == len(candidates) or total >target :
            return
        subset.append(candidates[i])
        backtrack(i,total+candidates[i])
        subset.pop()
        backtrack(i+1,total)
    backtrack(0,0)
    return res
candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates,target))

