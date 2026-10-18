def firstandlastoccurence(nums,target):
    def first_position():
        n =len(nums)
        low =0
        high = n-1
        first = n
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=target:
                first = mid
                high = mid-1
            else:
                low = mid+1
        return first 
    def last_position():
        n =len(nums)
        low = 0
        high = n-1
        last = n
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>target:
                last = mid
                high = mid -1
            else:
                low = mid +1
        return last
    fp = first_position()
    if fp == len(nums) or nums[fp]!=target:
        return [-1,-1]
    lp = last_position()
    return [fp,lp-1]
nums = [5,7,7,8,8,10]
target = 8
print(firstandlastoccurence(nums,target))
        