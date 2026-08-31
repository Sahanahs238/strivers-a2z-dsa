def intersection_arrays(arr1,arr2):
    s = set(arr1)
    ans = []
    for i in range(len(arr2)):
        if arr2[i] in s and arr2[i] not in ans :
            ans.append(arr2[i])
    return sorted(ans)
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(intersection_arrays(arr1,arr2))