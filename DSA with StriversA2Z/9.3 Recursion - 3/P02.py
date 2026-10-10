def combinationSum11(candidates,target):
    candidates.sort()
    subset =[]
    res=[]
    def backtrack(i,total):
        if total==target:
            res.append(subset.copy())
            return
        if i==len(candidates) or total > target:
            return
        subset.append(candidates[i])
        backtrack(i+1,total+candidates[i])
        subset.pop()
        while i+1 < len(candidates) and candidates[i]==candidates[i+1]:
            i+=1
        backtrack(i+1,total)
    backtrack(0,0)
    return res
candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum11(candidates,target))