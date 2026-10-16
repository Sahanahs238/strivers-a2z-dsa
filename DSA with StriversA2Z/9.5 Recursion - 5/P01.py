def partition(s):
    partition = []
    res =[]
    def backtrack(i):
        if i ==len(s):
            res.append(partition.copy())
            return
        for end in range(i,len(s)):
            part = s[i:end+1]
            if part == part[::-1]:
                partition.append(part)
                backtrack(end+1)
                partition.pop()
    backtrack(0)
    return res
s = "aab"
print(partition(s))