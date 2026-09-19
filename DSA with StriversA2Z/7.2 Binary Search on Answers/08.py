def canPlace(nums,k,d):
    count =1
    lastpos = nums[0]
    for i in range(1,len(nums)):
        if nums[i]-lastpos >= d:
            count +=1
            lastpos = nums[i]
            if count == k:
                return True
    return False
def aggresiveCows(nums,k):
    nums.sort()
    low = 1
    high = nums[-1]-nums[0]
    while low <= high:
        mid = (low+high)//2
        if canPlace(nums,k,mid):
            low = mid +1
        else:
            high =mid-1
    return high 
 
nums = [0, 3, 4, 7, 10, 9]
k =4
print(aggresiveCows(nums,k))
