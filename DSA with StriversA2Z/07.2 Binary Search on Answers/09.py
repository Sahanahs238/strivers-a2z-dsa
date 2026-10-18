def countStudents(nums,page_limit):
    students =1
    pages_count =0
    for pages in nums:
        if pages+pages_count <= page_limit:
            pages_count +=pages
        else:
            students +=1
            pages_count = pages
    return students
def findStudents(nums,m):
    low = max(nums)
    high = sum(nums)
    while low<=high:
        mid =(low+high)//2
        ans = countStudents(nums,mid)
        if ans > m:
            low = mid+1
        else:
            high = mid-1
    return low
nums = [12, 34, 67, 90]
m=2
print(findStudents(nums,m))