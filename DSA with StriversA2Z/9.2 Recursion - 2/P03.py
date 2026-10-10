def generateBinarystrings(n):
    cur =[]
    res =[]
    def backtrack():
        if len(cur)==n:
            res.append("".join(cur))
            return
        cur.append("0")
        backtrack()
        cur.pop()
        if not cur or cur[-1]!="1":
            cur.append("1")
            backtrack()
            cur.pop()
    backtrack()
    return res
n = 3
print(generateBinarystrings(n))