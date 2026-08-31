def reverse_array(arr,left,right):
    if left >= right :
        return
    arr[left],arr[right]=arr[right],arr[left]
    reverse_array(arr,left+1,right-1)
arr = [6,5,4,3,2,1]
reverse_array(arr,0,len(arr)-1)
print(arr)