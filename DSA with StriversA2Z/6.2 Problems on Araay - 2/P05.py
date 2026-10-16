def maxSubArray(nums):
        
        # maximum sum
    maxi = float('-inf') 
        
        # current sum of subarray
    summ = 0 
        
        # Iterate through the array
    for i in range(len(nums)):
            
            # Add current element to the sum
        summ += nums[i] 
            
            # Update maxi if current sum is greater
        if summ > maxi:
            maxi = summ 
            
            # Reset sum to 0 if it becomes negative
        if summ < 0:
            summ = 0 
        
        # Return the maximum subarray sum found
    return maxi
nums =[2, 3, 5, -2, 7, -4]
print(maxSubArray(nums))