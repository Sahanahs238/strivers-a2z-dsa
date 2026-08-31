def fibinocci(n):
    if n<= 1:
        return n
    return fibinocci(n-1)+fibinocci(n-2)
n = int(input("Enter a no :"))
print(fibinocci(n))