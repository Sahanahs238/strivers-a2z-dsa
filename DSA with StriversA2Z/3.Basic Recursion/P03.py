def printNumbers(n):
    if n==0:
        return
    printNumbers(n-1)
    print(n)

n =int(input("Enter a no:"))
printNumbers(n)