def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
n = int (input())
arr = list(map(int,input().split()))
print(bubble_sort(arr))