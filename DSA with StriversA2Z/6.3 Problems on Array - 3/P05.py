def maxlenzero(arr):
    d ={}
    s = 0
    res = 0
    for i in range(len(arr)):
        s += arr[i]
        if s not in d:
            d[s]=i
        else:
            res = max(res,i-d[s])
        if s==0:
            res = i+1
    return res
arr = list(map(int,input().split()))
print(maxlenzero(arr))