def rearrangesign(nums):
    ans = [0]*len(nums)
    pos_idx = 0
    neg_idx = 1
    for n in nums:
        if n>0:
            ans[pos_idx]=n
            pos_idx +=2
        else:
            ans[neg_idx]=n
            neg_idx+=2
    return ans
nums = list(map(int,input().split()))
print(rearrangesign(nums))
