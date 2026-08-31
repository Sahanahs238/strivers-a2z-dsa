def unique_elements(arr):
    unique = sorted(set(arr))
    print(unique)
arr = list(map(int,input().split()))
print(unique_elements(arr))