def findMin(arr):
    low = 0
    high = len(arr)-1
    ans = arr[0]
    while low<=high:
        if arr[low]<=arr[high]:
            ans = min(ans,arr[low])
            break
        mid = (low+high)//2
        if arr[low]<=arr[mid]:
            ans = min(ans,arr[low])
            low = mid +1
        else:
            high = mid-1
            ans = min(ans,arr[mid])
    return ans
arr = [3,4,5,1,2,0]
print(findMin(arr))