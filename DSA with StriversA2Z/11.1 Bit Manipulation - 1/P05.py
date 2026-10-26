def isPowerOfTwo(n):
    if (n & n-1 )==0:
        return True
    return False
n = 16
print(isPowerOfTwo(n))