def ArmStrong(n):
    original = n
    Sum = 0

    while n>0:
        last_digit=n%10
        Sum =Sum + (last_digit*last_digit*last_digit)
        n//=10
    return Sum == original
n = int(input("Enter a number:"))
print(ArmStrong(n))