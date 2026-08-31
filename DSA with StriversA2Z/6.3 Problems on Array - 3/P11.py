def max_product(nums):
    max_p=min_p=nums[0]
    maximum_product = max_p
    for n in nums[1:]:
        temp =max_p
        max_p = max(n*max_p,n*min_p,n)
        min_p = min(n*temp,n*min_p,n)
        maximum_product = max(max_p,maximum_product)
    return maximum_product
nums =[2,3,-2,4]
print(max_product(nums))