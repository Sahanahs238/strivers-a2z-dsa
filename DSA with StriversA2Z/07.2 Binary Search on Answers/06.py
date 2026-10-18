def dayNeeded(weights,capacity):
    days =1
    currentload =0
    for weight in weights:
        if currentload + weight > capacity:
            days +=1
            currentload = weight
        else:
            currentload += weight
    return days
def shipWithinDays(weights,days):
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid = (low+high)//2
        need = dayNeeded(weights,mid)
        if need <= days:
            high = mid-1
        else:
            low = mid +1
    return low
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(shipWithinDays(weights,days))
        