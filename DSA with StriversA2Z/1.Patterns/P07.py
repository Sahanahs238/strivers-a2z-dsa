for i in range(6):
    for j in range(6-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()