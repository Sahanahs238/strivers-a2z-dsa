def reverseStack(stack):
        # Your code goes here
    def insertfromBottom(stack,elem):
        if not stack:
            stack.append(elem)
            return
        top = stack.pop()
        insertfromBottom(stack,elem)
        stack.append(top)
    if not stack:
        return
    top = stack.pop()
    reverseStack(stack)
    insertfromBottom(stack,top)
    return stack
stack = [1,2,3,4]
print(reverseStack(stack))


        
