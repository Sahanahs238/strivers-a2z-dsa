import math
def calculateTotalHours(piles,speed):
    totalH =0
    for bananas in piles:
        totalH += math.ceil(bananas/speed)
    return totalH
def minbananas(piles,h):
    low = 1
    high = max(piles)
    ans = max(piles)
    while low<=high:
        mid =(low+high)//2
        totalH = calculateTotalHours(piles,mid)
        if totalH <= h:
            ans = mid
            high = mid-1
        else:
            low =mid+1
    return ans
piles = [7, 15, 6, 3]
h = 8
print(minbananas(piles,h))