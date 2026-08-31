for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print(" "*(8-(2*i)),end="")

    for j in range(i,0,-1):
        print(j,end=" ")
    print()