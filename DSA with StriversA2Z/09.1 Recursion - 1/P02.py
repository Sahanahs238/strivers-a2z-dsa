def generateParanthesis(n):
    stack =[]
    res=[]
    def backtracking(Open,close):
        if Open==close==n:
            res.append("".join(stack))
            return
        if Open<n:
            stack.append("(")
            backtracking(Open+1,close)
            stack.pop()
        if close <Open:
            stack.append(")")
            backtracking(Open,close+1)
            stack.pop()
    backtracking(0,0)
    return res
n = 3
print(generateParanthesis(n))