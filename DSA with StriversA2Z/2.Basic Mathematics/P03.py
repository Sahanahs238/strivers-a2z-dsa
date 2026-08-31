def reverse(x):
    if x<0:
        return False
    original = x
    reverse = 0

    while x> 0:
        last_digit= x%10
        x //= 10
        reverse = reverse*10 + last_digit
    return reverse == original
x=int(input("enter a number:"))
print(reverse(x))
