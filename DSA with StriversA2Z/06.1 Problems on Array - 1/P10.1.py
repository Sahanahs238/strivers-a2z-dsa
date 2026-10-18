def missing_number(arr):
    res = len(arr)
    for i in range(len(arr)):
        res += (i-arr[i])
    return res
arr = list(map(int,input().split()))
print(missing_number(arr))