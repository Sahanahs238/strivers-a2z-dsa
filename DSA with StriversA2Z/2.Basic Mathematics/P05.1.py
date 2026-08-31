def devisors(n):
    divisor = []

    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            divisor.append(i)
            if n//i != i:
                divisor.append(n//i)
    divisor.sort()
    return divisor
n = int(input("Enter a number:"))
print(devisors(n))

        