def second_largest(arr):
    largest = 0
    second_largest = 0
    n = len(arr)
    for i in range(1,n):
        if arr[i]>largest:
            second_largest =largest
            largest = arr[i]
        elif arr[i] < largest and arr[i]>second_largest:
            second_largest = arr[i]
    return second_largest
arr = list(map(int,input().split()))
print(second_largest(arr))