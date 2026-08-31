def reverse_array_by_k_times(arr,k):
    k = k%len(arr)
    l,r=0,len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l,r=l+1,r-1
    l,r=0,k-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l,r=l+1,r-1
    l,r=k,len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l,r=l+1,r-1
    return arr

k = int(input())
arr = list(map(int,input().split()))
print(reverse_array_by_k_times(arr,k))