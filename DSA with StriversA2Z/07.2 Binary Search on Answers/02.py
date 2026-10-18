def NthRoot(n,m):
    if m==0 or m==1:
        return m
    low =1
    high =m
    while low<=high:
        mid = (low+high)//2
        val = mid**n
        if val ==m:
            return mid
        elif val>m:
            high =mid-1
        else:
            low = mid+1
    return -1
n = 3
m = 27
print(NthRoot(n,m))