def twosum(nums,target):
    h = {}
    for i in range(len(nums)):
        h[nums[i]]=i
    for i in range(len(nums)):
        y = target - nums[i]
        if y in h and h[y]!=i:
            return [i,h[y]]
target = int(input("Enter target:"))
nums = list(map(int,input().split()))
print(twosum(nums,target))