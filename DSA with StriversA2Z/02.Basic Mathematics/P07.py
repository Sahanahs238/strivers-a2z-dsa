n1 =int(input("Enter a number:"))
print(n1)
n2 =int(input("Enter another number:"))
print(n2)
for i in range(min(n1,n2),0,-1):
    if(n1%i==0 and n2%i==0):
        print("GCD:",i)
        break