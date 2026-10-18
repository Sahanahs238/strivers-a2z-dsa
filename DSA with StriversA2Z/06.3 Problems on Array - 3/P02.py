def mejorityelement2(nums):
    cand1,count1 = None,0
    cand2,count2=None,0
    for n in nums:
        if cand1 ==n:
            count1 += 1
        elif cand2 == n:
            count2 += 1
        elif count1 == 0:
            cand1 = n
            count1 +=1
        elif count2 == 0:
            cand2 = n
            count2 += 1
        else:
            count1,count2 =count1 - 1,count2-1
    return [ x for x in (cand1,cand2) if nums.count(x)>len(nums)//3]
nums = list(map(int,input().split()))
print(mejorityelement2(nums))