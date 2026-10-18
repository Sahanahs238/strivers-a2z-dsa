def findrotate(arr):
    low =0
    high =len(arr)-1
    ans = arr[0]
    index = 0
    while low<=high:
        if arr[low]<=arr[high]:
            if arr[low]<ans:
                ans = arr[low]
                index = low 
            break
        mid =(low+high)//2
        if arr[low]<=arr[mid]:
            if arr[low]<ans:
                ans= arr[low]
                index =low
            low =mid+1
        else:
            if arr[mid]<ans:
                ans =arr[mid]
                index = mid
            high = mid-1
    return index
arr = [3, 4, 5, 0, 1, 2]  
print(findrotate(arr))   
