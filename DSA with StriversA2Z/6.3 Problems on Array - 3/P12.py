def countSubarraysWithXorK(arr, k):
    xor_map = {0: 1}
    
    current_xor = 0
    count = 0
    
    for num in arr:

        current_xor ^= num
        target_xor = current_xor ^ k
        if target_xor in xor_map:
            count += xor_map[target_xor]
        if current_xor in xor_map:
            xor_map[current_xor] += 1
        else:
            xor_map[current_xor] = 1
        
    return count
arr = [4, 2, 2, 6, 4]
k = 6
print(f"Total subarrays with XOR {k}: {countSubarraysWithXorK(arr, k)}")

