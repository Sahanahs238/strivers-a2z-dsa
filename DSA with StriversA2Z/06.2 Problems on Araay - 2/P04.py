def majorityElement(nums):
    n = len(nums)
    cnt = 0
    el = 0
    for num in nums:
        if cnt == 0:
            cnt = 1
            el = num
        elif el == num:
            cnt += 1
        else:
            cnt -= 1
        
    cnt1 = nums.count(el)
        
    if cnt1 > (n // 2):
        return el
        
        # Return -1 if no such element found
    return -1
nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
