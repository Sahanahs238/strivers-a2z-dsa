def printNumbers(n):
    if n==0:
        return
    print(n)
    printNumbers(n-1)


n =int(input("Enter a no:"))
printNumbers(n)