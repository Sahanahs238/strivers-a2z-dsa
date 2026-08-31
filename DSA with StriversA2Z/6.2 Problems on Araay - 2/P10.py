def longestConsecuitive(nums):
    snums = set(nums)
    longest = 0
    for n in nums:
        if (n-1) not in snums:
            length = 0
            while (n+length) in snums:
                length += 1
            longest = max(longest,length)
    return longest
nums = list(map(int,input().split()))
print(longestConsecuitive(nums))