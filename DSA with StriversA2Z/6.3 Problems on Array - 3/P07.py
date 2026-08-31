def merge(nums1,m,nums2,n):
    insert = len(nums1)-1
    p1 = m-1
    p2 = n-1
    while p1 >= 0 and p2>=0:
        n1 =nums1[p1]
        n2 =nums2[p2]
        if n1>n2:
            nums1[insert]=n1
            p1-=1
        else:
            nums1[insert]=n2
            p2-=1
        insert -= 1
    while p2 >=0 :
        nums1[insert]=nums2[p2]
        p2-=1
        insert -= 1
    return nums1
m = int(input("Enter number of active elements in nums1 (m): "))
n = int(input("Enter number of elements in nums2 (n): "))
print(f"Enter {m} numbers for nums1 separated by spaces:")
nums1 = list(map(int, input().split()))
nums1.extend([0] * n)
print(f"Enter {n} numbers for nums2 separated by spaces:")
nums2 = list(map(int, input().split()))
print("Merged array inside nums1:", merge(nums1, m, nums2, n))