def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            #Starting at i + 1 guarantees that j is always at least one step ahead of i
            if nums[i]+nums[j]==target:
                return [i,j]
target = int(input("Enter target: "))
nums = list(map(int,input().split()))
print(twosum(nums,target))