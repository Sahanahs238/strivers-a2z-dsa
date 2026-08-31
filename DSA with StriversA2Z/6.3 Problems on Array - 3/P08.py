def findmissingandrepeating(nums):
    n  = len(nums)
    count = [0]*(n+1)
    for num in nums:
        count[num] += 1
    repeating = -1
    missing = -1
    for i in range(1,n+1):
        if count[i]==2:
            repeating = i
        elif count[i]==0:
            missing = i
    return [repeating,missing]
nums = [3, 5, 4, 1, 1]
print(findmissingandrepeating(nums))