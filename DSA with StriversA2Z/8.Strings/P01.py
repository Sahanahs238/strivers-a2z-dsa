def removeOuterParentheses(s):
        # Your code goes here
    counter = 0
    res = []
    for char in s:
        if char == "(":
            if counter >0:
                res.append(char)
            counter+=1
        else:
            counter-=1
            if counter >0:
                res.append(char)
    return "".join(res)
s = "((()))"
print(removeOuterParentheses(s))

