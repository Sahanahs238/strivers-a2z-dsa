def is_possible(bloom_days,day,m,k):
    count =0
    bouquet = 0
    for bloom in bloom_days :
        if bloom <= day:
            count +=1
            if count ==k:
                bouquet +=1
                count =0
        else:
            count =0
    return bouquet >= m
def mindays(bloom_days,m,k):
    if m*k > len(bloom_days):
        return -1
    low = min(bloom_days)
    high = max(bloom_days)
    ans = max(bloom_days)
    while low<= high:
        mid = (low+high)//2
        if is_possible(bloom_days,mid,m,k):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans
bloom_days = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2 #bouquets
k = 3 #flowers
print(mindays(bloom_days,m,k))