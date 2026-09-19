def findkthelement(nums1,nums2,k):
    if len(nums1)>len(nums2):
        nums1,nums2=nums2,nums1
    n1 = len(nums1)
    n2 = len(nums2)
    low = max(0,k-n1)
    high = min(k,n1)
    left = k
    while low <= high :
        mid1 = (low+high)//2
        mid2 = left - mid1
        l1,l2 = float('-inf'),float('-inf')
        r1,r2=float('inf'),float('inf')
        if mid1 <n1:
            r1 = nums1[mid1]
        if mid2 <n2:
            r2 =nums2[mid2]
        if mid1-1 >= 0:
            l1 = nums1[mid1-1]
        if mid2-1 >= 0:
            l2 = nums2[mid2-1]
        if l1 <=r2 and l2 <= r1:
            return max(l1,l2)
        elif l1>r2:
            high = mid1-1
        else:
            low = mid1+1
    return -1 
nums1 = [2, 3, 6, 7, 9]
nums2= [1, 4, 8, 10]
k = 5
print(findkthelement(nums1,nums2,k))
        
