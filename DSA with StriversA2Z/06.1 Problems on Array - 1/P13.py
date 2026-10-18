def max_subarray(arr,k):
    d = {}
    count = 0
    Sum = 0
    for number in arr:
        Sum += number
        if Sum == k:
            count+=1
        if (Sum - k) in d:
            count += d[Sum-k]
        d[Sum]=d.get(Sum,0)+1
    return count
k = int (input("Enter the sum:"))
arr = list(map(int,input().split()))
print(max_subarray(arr,k))
