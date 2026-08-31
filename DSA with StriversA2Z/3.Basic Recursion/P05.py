def print_1_to_n(i, n):
    if i < 1:
        return

    print_1_to_n(i - 1, n)
    print(i)

n = int(input("Enter n: "))
print_1_to_n(n, n)