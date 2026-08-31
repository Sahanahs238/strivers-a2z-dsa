def floorandceil(nums,x):
    low = 0
    high =len(nums)-1
    floor =-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid]<=x:
            floor = nums[mid]
            low = mid +1
        else:
            high =mid -1
    low =0
    high = len(nums)-1
    ceil = len(nums)
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=x:
            ceil = nums[mid]
            high = mid -1
        else:
            low = mid +1
    return [floor,ceil]
nums = [3, 4, 4, 7, 8, 10]
x= 5
print(floorandceil(nums,x))