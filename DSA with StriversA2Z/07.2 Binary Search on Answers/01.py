def findsqrt(n):
    low = 1
    high = n
    while low<=high:
        mid = (low+high)//2
        ans = mid*mid
        if ans <= n:
            low = mid+1
        else:
            high = mid-1
    return high
n = 36
print(findsqrt(n))