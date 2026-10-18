def sum_n_to_1(n):
    if n == 0:
        return 0
    return n + sum_n_to_1(n-1)
n= int(input("Enter a number:"))
print(sum_n_to_1(n))