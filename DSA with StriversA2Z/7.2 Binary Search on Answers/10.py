def partition(a,array_limit):
    # same as previus
    partitions =1
    Sum =0
    for num in a:
        if num+Sum <=array_limit:
            Sum += num
        else:
            partitions +=1
            Sum = num
    return partitions
def largestSubarraySumMinimized(a, k):
    low = max(a)
    high =sum(a)
    while low <= high:
        mid = (low+high)//2
        ans = partition(a,mid)
        if ans > k:
            low = mid +1
        else:
            high = mid-1
    return low
a =[1, 2, 3, 4, 5]
k = 3
print(largestSubarraySumMinimized(a, k))
# q, painters partition also same
        