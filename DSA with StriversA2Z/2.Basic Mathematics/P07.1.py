a= int(input("Enter a number:"))
b =int(input("Enter another number:"))
while a>0 and b>0:
    if a>b:
        a=a%b
    else:
        b=b%a

if(a==0):
    print(b)
else:
    print(a)