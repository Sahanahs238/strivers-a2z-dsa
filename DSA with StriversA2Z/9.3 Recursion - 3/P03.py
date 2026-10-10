def combinationSum3(k,n):
    subset = []
    res=[]
    def backtrack(i,total):
        if len(subset)==k and total ==n:
            res.append(subset.copy())
            return 
        if len(subset)>=k and total >n:
            return
        for num in range(i,10):
            subset.append(num)
            backtrack(num+1,total+num)
            subset.pop()
    backtrack(1,0)
    return res
k = 3
n = 7
print(combinationSum3(k,n))