def swap(a,b):
    a= a^b
    b=a^b
    a=a^b
    return a,b
a= 5
b= 10
print(swap(a,b))