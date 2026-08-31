def is_sorted(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            return False
    return True 
arr = list(map(int,input().split()))
print(is_sorted(arr))