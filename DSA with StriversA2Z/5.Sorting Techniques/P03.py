def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j =i 
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr
n =int(input())
arr = list(map(int,input().split()))
print(insertion_sort(arr))
