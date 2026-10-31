def minBitsFlip(start, goal):
    n = start^goal 
    count = 0
    while n:
        count += n&1
        n = n>>1
    return count
start = 10
goal = 7
print(minBitsFlip(start,goal))