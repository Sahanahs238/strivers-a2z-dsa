def sum_1_to_n(n, total):
    if n == 0:
        return total

    total += n
    return sum_1_to_n(n - 1, total)

n = int(input("Enter a number: "))
print(sum_1_to_n(n, 0))