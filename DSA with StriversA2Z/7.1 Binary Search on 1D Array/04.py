def search_insert_position(nums,x):
    #completely same as lower bound
    low = 0
    high = len(nums) - 1
    ans  = len(nums)
    while low <= high:
        mid = (low+high)//2
        if nums[mid]>=x:
            ans = mid
            high = mid-1
        else:
            low = mid +1
    return ans
nums = [1,2,2,3]
x =2
print(search_insert_position(nums,x))