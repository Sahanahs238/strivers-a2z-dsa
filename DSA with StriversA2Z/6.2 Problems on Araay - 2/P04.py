def mejorityElement(nums):
    count,res=0,0
    for n in nums:
        if count == 0:
            res = n
            count += (1 if res==n else -1)
    return res
nums = list(map(int,input().split()))
print(mejorityElement(nums))