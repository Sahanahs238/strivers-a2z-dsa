for i in range(4):
    for j in range(3-i):
        print(" ",end="")
    for j in range(i+1):
        print(chr(65+j),end="")
    for j in range(i-1,-1,-1):
        print(chr(65+j),end="")
    print()