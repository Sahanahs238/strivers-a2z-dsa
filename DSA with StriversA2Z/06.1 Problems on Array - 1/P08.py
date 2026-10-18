def union_of_two_sorted_arrays(arr1,arr2,n,m):
    i,j=0,0
    ans = []
    while i<n and j<m:
        if arr1[i]==arr2[j]:
            if len(ans)==0 or ans[-1]!=arr1[i]:
                ans.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            if len(ans)==0 or ans[-1]!=arr1[i]:
                ans.append(arr1[i])
            i+=1
        else:
            if len(ans)==0 or ans[-1]!=arr2[j]:
                ans.append(arr2[j])
            j+=1
    while i<n:
        if len(ans)==0 or ans[-1]!=arr1[i]:
            ans.append(arr1[i])
        i+=1
    while j<m:
        if len(ans)==0 or ans[-1]!=arr2[j]:
            ans.append(arr2[j])
        j+=1
    return ans
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
print(union_of_two_sorted_arrays(arr1,arr2,len(arr1),len(arr2)))