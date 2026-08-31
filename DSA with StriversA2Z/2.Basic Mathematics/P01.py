def count(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt

n = int(input("Enter a number: "))
print(count(n))