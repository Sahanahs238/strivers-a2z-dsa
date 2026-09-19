def missingK(arr,k):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        missing = arr[mid]-(mid+1)
        if missing < k:
            low =mid+1
        else:
            high =mid-1
    return k+high+1 #or k+low bcoz,low=high+1
# formulae k+high+1 derivation , we hv to return (high +more) more=k-missing 
# sub, (arr[high]+more)
      # (arr[high] + (k-missing))
# sub missing , arr[high] +(k-(arr[high]-(high+1)))
               # arr[high] + k -arr[high]+high+1
# on cancelling, k+high+1 == k+low
arr = [3, 5, 7, 10]
k = 6
print(missingK(arr,k))