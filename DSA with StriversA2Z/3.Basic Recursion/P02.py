def print_name(n):
    if n == 0:
        return

    print("sahana")
    print_name(n - 1)

n = int(input("Enter a number: "))
print_name(n)