def maxDepth(s):
        # Your code goes here
    res = 0
    counter = 0
    for char in s:
        if char == "(":
            counter += 1
            res = max(res,counter )
        elif char == ")":
            counter -= 1
    return res
s ="(1+(2*3)+((8)/4))+1"
print(maxDepth(s))