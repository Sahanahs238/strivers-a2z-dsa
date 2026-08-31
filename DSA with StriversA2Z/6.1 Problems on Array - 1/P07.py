def linear_search(arr):
    target = int(input("Enter the target: "))
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr = list(map(int,input().split()))
print(linear_search(arr))