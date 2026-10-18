def move_zeros_to_end(arr):
    j =0 
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    return arr
arr = list(map(int,input().split()))
print(move_zeros_to_end(arr))