def largestElement(arr):
    n = len(arr)
    largest = arr[0]
    for i in range(1,n):
        if arr[i]>largest:
            largest = arr[i]
    return largest
arr = list(map(int,input().split()))
print(largestElement(arr))
