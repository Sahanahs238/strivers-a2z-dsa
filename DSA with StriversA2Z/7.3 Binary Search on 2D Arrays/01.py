def lower_bound(arr,x):
    n = len(arr)
    low =0
    high = n-1
    ans = n
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=x:
            ans = mid
            high = mid -1
        else:
            low = mid+1
    return ans
def max_ones(mat):
    n = len(mat)
    m = len(mat[0])
    count_max = 0
    index = -1
    for i in range(n):
        count_ones = m-lower_bound(mat[i],1)
        if count_ones > count_max:
            count_max = count_ones 
            index = i
    return index
mat = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]
print(max_ones(mat))