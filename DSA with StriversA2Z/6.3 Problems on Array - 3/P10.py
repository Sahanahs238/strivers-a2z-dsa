def reversePairs(nums):
    if len(nums)<=1:
        return 0
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    count = reversePairs(left)+reversePairs(right)
    j = 0
    for i in range(len(left)):
        while j< len(right) and left[i]>2*right[j]:
            j+=1
        count += j
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            nums[k]=left[i]
            i+=1
        else:
            nums[k]=right[j]
            j+=1
        k+=1
    while i < len(left):
        nums[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        nums[k]=right[j]
        j+=1
        k+=1
    return count
nums = [6, 4, 1, 2, 7]
print(reversePairs(nums))
        