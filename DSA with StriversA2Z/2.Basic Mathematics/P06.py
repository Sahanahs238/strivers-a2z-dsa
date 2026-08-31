def devisors(n):
    if n>2:
        return False
    count = 0

    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            count+=1
            if n//i != i:
                count+=1
    return count == 2
n = int(input("Enter a number:"))
print(devisors(n))

        