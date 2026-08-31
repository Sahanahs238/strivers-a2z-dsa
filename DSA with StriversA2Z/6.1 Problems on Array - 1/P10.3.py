def missing_number_xor(arr):
    n =len(arr)
    xor1 = 0
    xor2 = 0
    for num in arr:
        xor1 = xor1^num
    for i in range(n+1):
        xor2 = xor2^i
    return xor1^xor2
arr = list(map(int,input().split()))
print(missing_number_xor(arr))