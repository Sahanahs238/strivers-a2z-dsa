def lower_bound(nums,x):
    #smallest in nums greater than or equal to x
    low = 0
    high = len(nums) - 1
    ans  = len(nums) #default answer is the last element
    while low <= high:
        mid = (low+high)//2
        if nums[mid]>=x:
            ans = mid
            # to check if there is a duplicate exists before
            high = mid-1
        else:
            low = mid +1
    return ans
nums = [1,2,2,3]
x =2
print(lower_bound(nums,x))