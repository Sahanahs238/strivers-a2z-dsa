def search2(nums,target):
    #duplicates
    low =0
    high = len(nums)-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return True
        if nums[mid]==nums[low]==nums[high]:
            low+=1
            high-=1
            continue
        if nums[low]<nums[mid]:
            if target >=nums[low] and target <nums[mid]:
                high = mid -1
            else:
                low = mid +1
        else:
            if target >nums[mid] and target <= nums[high]:
                low = mid+1
            else:
                high = mid -1
    return False
nums =[2,5,6,0,0,1,2]
target = 0
print(search2(nums,target))