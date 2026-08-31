def count_inversions(nums):
    if len(nums)<=1:
        return 0
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid: ]
    count = count_inversions(left)+count_inversions(right)
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            nums[k]=left[i]
            i+=1
        else:
            nums[k]=right[j]
            j+=1
            count += (len(left)-i)
        k+=1
    while i<len(left):
        nums[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        nums[k]=right[j]
        j+=1
        k+=1
    return count
nums =[2, 3, 7, 1, 3, 5]
print(count_inversions(nums))