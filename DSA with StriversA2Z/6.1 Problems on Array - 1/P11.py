def max_consecuitives(arr):
    Sum = 0
    maxi = 0
    for num in arr:
        if num == 0:
            Sum = 0
        else:
            Sum += 1
            maxi = max(maxi,Sum)
    return maxi
arr = list(map(int,input().split()))
print(max_consecuitives(arr))