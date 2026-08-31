def reverse(x):
    reverse = 0
    sign = -1 if x<0 else 1
    x = abs(x)

    while x> 0:
        last_digit= x%10
        x //= 10
        reverse = reverse*10 + last_digit
    return sign*reverse
x=int(input("enter a number:"))
print(reverse(x))
