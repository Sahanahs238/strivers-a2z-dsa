def mergesort(arr):
    if len(arr)<=1:
        return arr
    
    mid= len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    result = []
    i =0
    j =0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j: ]
    return result
n =int(input())
arr = list(map(int,input().split()))
print(mergesort(arr))
